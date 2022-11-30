# learning-protocol-buffers

https://developers.google.com/protocol-buffers/docs/pythontutorial

# Why am I learning this?

<blockquote>Data Contracts</blockquote>

I recently learned about building streaming applications with Apache Kafka. Kafka has a component called a Schema registry that can be used to track schema evolution. I'm very interested in learning how this works because I believe that knowing the structure of incoming data can potentially eliminate some overhead associated with the maintainance of data pipelines. 

## ... But aren't there are other serialization methods?
True, but I've heard about the level of compression that protocol buffers provide. So, I want to take advantage of this capability and develop data contracts in my future projects. 


<br/>

I'll be following google's tutorial for an introduction to the technology. 

# Problem

I want to develop a very simple address book application that can read and write people's contact details to and from a file. Each person in the address book has a name, and ID, an email address, and a contact phone number. Despite other serialization methods, I want to use protocol buffers for serialization and retrieval of the contact information. 

<br/>

```bash 
./protoc-21.9-osx-aarch_64/bin/protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto
```
