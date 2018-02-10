/**
 * Created by slience-pc on 2018/2/7.
 */


!function c(n) {
            var i = "__bdpp_pstc__" + (new Date).getTime()
              , s = i + "_form"
              , o = i + "_ifr"
              , r = function(e) {
                if ("object" == typeof e) {
                    var t = [];
                    for (var n in e) {
                        var i = e[n];
                        if (void 0 !== i && null !== i) {
                            t.length && t.push("&");
                            var s = encodeURIComponent("boolean" == typeof i ? i ? "1" : "0" : i.toString());
                            t.push(encodeURIComponent(n), "=", s)
                        }
                    }
                    return t.join("")
                }
                return "string" == typeof e ? e : null
            }
              , a = function(e, t) {
                if (t = r(t),
                "string" == typeof t) {
                    var n = /\?/g.test(e);
                    e += (n ? "&" : "?") + r(t)
                }
                return e
            }
              , l = function(e, t, n) {
                e.setAttribute("type", "text/javascript"),
                n && e.setAttribute("charset", n),
                e.setAttribute("src", t),
                document.getElementsByTagName("head")[0].appendChild(e)
            }
              , d = function(e) {
                if (e.clearAttributes)
                    e.clearAttributes();
                else
                    for (var t in e)
                        e.hasOwnProperty(t) && delete e[t];
                e && e.parentNode && e.parentNode.removeChild(e),
                e = null
            }
              , u = function(e, t, n) {
                function i(e) {
                    return function() {
                        try {
                            e ? u.onfailure && u.onfailure() : (t.apply(window, arguments),
                            clearTimeout(o)),
                            window[s] = null,
                            delete window[s]
                        } catch (n) {} finally {
                            d(r)
                        }
                    }
                }
                var s, o, r = document.createElement("SCRIPT"), a = "bd__cbs__", u = n || {}, p = u.charset, g = u.queryField || "callback", h = u.timeOut || 0, f = new RegExp("(\\?|&)" + g + "=([^&]*)");
                s = c.getUniqueId(a),
                window[s] = i(0),
                h && (o = setTimeout(i(1), h)),
                e = e.replace(f, "$1" + g + "=" + s),
                e.search(f) < 0 && (e += (e.indexOf("?") < 0 ? "?" : "&") + g + "=" + s),
                l(r, e, p)
            }
              , p = function(e, t) {
                var n = [];
                n.push("<form id='", s, "' target='", o, "' "),
                n.push("action='", c.encodeHTML(e), "' method='post'>");
                for (var i in t)
                    if (t.hasOwnProperty(i)) {
                        var r = t[i];
                        if (void 0 !== r && null !== r) {
                            var a = c.encodeHTML("boolean" == typeof r ? r ? "1" : "0" : r);
                            n.push("<input type='hidden' name='", c.encodeHTML(i), "' value='", a, "' />")
                        }
                    }
                return n.push("</form>"),
                n.join("")
            }
              , g = function(e, t, n, r) {
                function a(e) {
                    return function() {
                        try {
                            e ? r.onfailure && r.onfailure() : (n.apply(window, arguments),
                            d && clearTimeout(d)),
                            window[u] = null,
                            delete window[u]
                        } catch (t) {}
                    }
                }
                r = r || {};
                var l = r.timeOut || 0
                  , d = !1
                  , u = c.getUniqueId("bd__pcbs__");
                t[r.queryField || "callback"] = "parent." + u;
                var g = p(e, t);
                if (c.g(s))
                    c.getParent(s).innerHTML = g;
                else {
                    var h = [];
                    h.push("<div id='", i, "' style='display:none;'>"),
                    h.push("<div>", g, "</div>"),
                    h.push("<iframe name='", o, "' src='" + ("https:" == (window.location ? window.location.protocol.toLowerCase() : document.location.protocol.toLowerCase()) ? "https://passport.baidu.com/passApi/html/_blank.html" : "about:blank") + "' style='display:none;'></iframe>"),
                    h.push("</div>"),
                    c.insertHTML(document.body, "beforeEnd", h.join(""))
                }
                window[u] = a(),
                l && (d = setTimeout(a(1), l)),
                c.g(s).submit()
            };
            n.jsonp = function(n, i, s) {
                return s = s || {},
                e && e.traceID && e.traceID.createTraceID && (i.traceid = e.traceID.createTraceID()),
                new t(function(e, t) {
                    n = a(n, i),
                    u(n, function(t) {
                        s.processData && (t = s.processData(t)),
                        e && e(t)
                    }, {
                        charset: s.charset,
                        queryField: s.queryField,
                        timeOut: s.timeOut,
                        onfailure: function() {
                            t && t()
                        }
                    })
                }
                )
            }
            ,
            n.submit = function(n, i, s) {
                return e && e.traceID && e.traceID.createTraceID && (i.traceid = e.traceID.createTraceID()),
                n && i ? new t(function(e) {
                    g(n, i, function(t) {
                        s.processData && (t = s.processData(t)),
                        e && e(t)
                    }, s)
                }
                ) : void 0
            }
            ;
            var h = [];
            n.load = function(e) {
                return new t(function(t) {
                    var n = h.push(new Image) - 1
                      , i = !1
                      , s = setTimeout(function() {
                        i = !0,
                        t && t()
                    }, 1e3);
                    h[n].onload = function() {
                        clearTimeout(s),
                        i || t && t(),
                        i = !0,
                        h[n] = h[n].onload = null
                    }
                    ,
                    h[n].src = e
                }
                )
            }
        }(l);