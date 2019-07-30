input{
couchdb_changes{
db=> "japon"
} }
output {
elasticsearch{
index => "japon"
}
}