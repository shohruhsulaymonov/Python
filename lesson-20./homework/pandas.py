import sqlite3
import pandas as pd

# HW1
#1
#import all the necessary data from the fule
with sqlite3.connect('chinook.db') as conn:
    invoices = pd.read_sql('SELECT * FROM Invoice', conn)
    customers = pd.read_sql('SELECT * FROM Customer', conn)

#Finds total spending of each customer for all time
total_spent = invoices[['CustomerId', 'Total']].groupby('CustomerId').sum()
#create a new colum with joined first andlast  names to make full names
customers['FullName'] = customers['FirstName'] + ' ' + customers['LastName']
#Keep only customer Id and their names
customers_names = customers[['CustomerId', 'FullName']]
#set customerId as index
customers_names.set_index('CustomerId', inplace=True)
#joins customer names with their corresponding total spent values, sorts values from highest to lowest and keeps only top 5
pd.concat((customers_names, total_spent), axis=1).sort_values(['Total'], ascending=False).head(5)



#import all the necessary data from the fule
with sqlite3.connect('chinook.db') as con:
    tracks = pd.read_sql('select * from track', con)
    albums = pd.read_sql('select * from album', con)
    invoices = pd.read_sql('select * from invoice', con)
    invoicelines = pd.read_sql('select * from invoiceline', con)

#Calculates how many track there are in each album
tracks_per_album = tracks.merge(albums, on='AlbumId').groupby('AlbumId')['TrackId'].nunique(dropna=True)
tracks_per_album.rename('TrackCount', inplace=True)
#Filtering out albums with only 1 track because it's ambigious whether it should be a single track or a full album.
tracks_per_album = tracks_per_album[tracks_per_album > 1] 
#Joins tracks to invoicelines df and finds how many tracks of each album was purchased in eack invoice
invoice_album_track_counts = invoicelines.merge(tracks, on='TrackId')
invoice_album_counts = invoice_album_track_counts.groupby(['InvoiceId', 'AlbumId'])['TrackId'].nunique()

invoice_album_counts = invoice_album_counts.rename('TotalAlbumTracks').reset_index()
#Merges two dfs and finds whether a customer bought a single track or an album per invoice
full_merged_invoice = invoice_album_counts.merge(tracks_per_album.reset_index(), on='AlbumId')
full_merged_invoice['IsFullAlbumPurchase'] = full_merged_invoice['TrackCount'] == full_merged_invoice['TotalAlbumTracks']

#Joins cutomerId column to find how many customers fall into which of the two categories
cust_pref = full_merged_invoice.merge(invoices[['InvoiceId', 'CustomerId']], on='InvoiceId')[['CustomerId', 'IsFullAlbumPurchase']]
#Finda whther a customer has ever bough a full album
cust_pref = cust_pref.groupby('CustomerId')['IsFullAlbumPurchase'].any().reset_index()
#Total number of customers
total_cust = cust_pref['CustomerId'].nunique()
#Number of cutomers that bough individual tracks
individual_track_cust = (cust_pref['IsFullAlbumPurchase'] == False).sum()

#The percentage
percentage = (individual_track_cust/total_cust*100)
#Summary
print(f"{percentage:.2f}% of customers prefer to buy individual tracks.")
print(f"{100 - percentage:.2f}% of customers prefer to buy full albums.")
