
// use to read in flask session cookie
// requires  jquery, cookie.js and paco (to unzip)
function parse_session() {
    var cookie = Cookies.get('session');
    if (!cookie) return;
    // Is the content ziped ?
    var un_64 = "";
    if (cookie[0] == ".") {
        var data = cookie.split('.')[1].replace(/_/g, '/').replace(/-/g, '+');
        un_b64 = atob(data);
        un_b64 = pako.inflate(un_b64, { to: 'string' });
    } else {
        var data = cookie.split('.')[0].replace(/_/g, '/').replace(/-/g, '+');
        un_b64 = atob(data);
    }
    return jQuery.parseJSON(un_b64);
}