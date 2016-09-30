BEGIN {
    RS = "";
    FS = "\n";
}
match($0, /^import \(.*/) {
    print substr($0, RSTART, RLENGTH)
}
match($0, /^import \".*\"/) {
    print substr($0, RSTART, RLENGTH)
}
