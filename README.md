# How to use
- Open or use a `port` of your choice and specify it in the script.
- Note the server's `IP`.
- Create the link. Example : `http://serverip:serverport/keyword` where `keyword` can be anything like the name of a person or group.
- Send the link to someone on Discord and you will know when they open it in the server log.

You can also send the receipt by email by including an image via URL in the body of the email.

# How it works
The script creates a TCP server serving a PNG file of size 1x1 over HTTP. 

Discord directly displays to the user an image contained in a url when they open a message, so when the user opens your message, a GET request will be sent from their Discord client to your server and your server will display the acknowledgement.

It works exactly the same way with e-mail.
