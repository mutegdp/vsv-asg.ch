function add(td) {
    if ((test = /eval\("(.*)\);/.exec(td))) {
        while (test[1].indexOf('\\') != -1) test[1] = test[1].replace('\\', '');
        eval(test[1] + ");");
        td = d;
    }

    return td
}