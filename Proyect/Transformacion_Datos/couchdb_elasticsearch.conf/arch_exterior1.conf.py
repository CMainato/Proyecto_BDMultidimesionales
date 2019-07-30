input{
couchdb_changes{
db=> "exterior1"
} }
output {
elasticsearch{
index => "exterior1"
}
}