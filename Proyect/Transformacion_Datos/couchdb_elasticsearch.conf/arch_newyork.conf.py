input{
couchdb_changes{
db=> "newyork"
} }
output {
elasticsearch{
index => "newyork"
}
}