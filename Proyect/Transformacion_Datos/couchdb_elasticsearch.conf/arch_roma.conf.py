input{
couchdb_changes{
db=> "roma"
} }
output {
elasticsearch{
index => "roma"
}
}