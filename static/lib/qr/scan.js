var i = this.id, s = window.google_iframe_oncopy, H = s && s.handlers, h = H && H[i], w = this.contentWindow, d;
try {
    d = w.document
} catch (e) {}
if (h && d && (!d.body || !d.body.firstChild)) {
    if (h.call) {
        setTimeout(h, 0)
    } else if (h.match) {
        try {
            h = s.upd(h, i)
        } catch (e) {}
        w.location.replace(h)
    }
}
