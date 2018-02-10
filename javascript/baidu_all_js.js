 passport.data = passport.data || {}, function(e) {
        function t(e) {
            this._requests = [],
            this._value = null,
            this._exception = null,
            this._isComplete = !1;
            var t = this;
            e(function(e) {
                t._fulfillPromise(e)
            }, function(e) {
                t._breakPromise(e)
            })
        }
        function n(e, t, n) {
            return t ? n ? function(n) {
                return n = n || {},
                l.submit(d + t, i(n, e, g[e], h[e], !0), {
                    charset: "utf-8",
                    processData: function(t) {
                        if (t)
                            for (var n in t)
                                if (t.hasOwnProperty(n)) {
                                    var i = t[n];
                                    i && (t[n] = decodeURIComponent(i))
                                }
                        return s(e, t)
                    }
                })
            }
            : function(n) {
                return l.jsonp(d + t, i(n, e, g[e], h[e], !1), {
                    charset: "utf-8",
                    processData: function(t) {
                        return s(e, t)
                    }
                })
            }
            : a
        }
        function i(e, t, n, i, s) {
            var o = s ? {
                staticpage: E.staticPage,
                charset: E.charset || document.characterSet || document.charset || ""
            } : {}
              , r = f[t];
            if (r)
                for (var a in r) {
                    if (r.hasOwnProperty(a)) {
                        var l = r[a];
                        o[a] = "function" == typeof l ? l(e) : l
                    }
                    "verifypass" == a && (o[a] = decodeURIComponent(o[a]))
                }
            if (o.token = E.token,
            o.tpl = E.product || "",
            o.subpro = E.subpro,
            o.apiver = "v3",
            o.tt = (new Date).getTime(),
            e) {
                n = n || {},
                i = i || {};
                for (var a in e)
                    if (e.hasOwnProperty(a)) {
                        var d = i[a]
                          , u = d ? d(e[a], e) : e[a];
                        "string" == typeof u && (s && (u = decodeURIComponent(u)),
                        m[a] || (u = c.trim(u))),
                        o[n[a] || a.toLowerCase()] = u
                    }
            }
            return o
        }
        function s(t, n) {
            if (e && e.traceID && e.traceID.getTraceID && e.traceID.getTraceID(n),
            n) {
                var i = v[t];
                i && i(n);
                var s = n.errInfo
                  , r = n
                  , a = r;
                return s ? r.errInfo = o(t, s, r) : (s = {
                    no: n.err_no,
                    msg: n.err_msg || ""
                },
                delete r.err_no,
                delete r.err_msg,
                a = {
                    data: r,
                    errInfo: o(t, s, r)
                }),
                a
            }
            return n
        }
        function o(e, t) {
            var n = y[b[e] || e];
            if (n && t && 0 != t.no) {
                var i = n[t.no] || n[-1];
                if (i) {
                    var s = i.msg;
                    t.msg = s,
                    t.field = i.field
                }
            }
            return t
        }
        function r(t) {
            if (e && e.traceID && e.traceID.getTraceID && e.traceID.getTraceID(t),
            t) {
                var n = t.errInfo
                  , i = t;
                if (!n)
                    for (var s in t)
                        if (t.hasOwnProperty(s)) {
                            var o = t[s];
                            o && (t[s] = decodeURIComponent(o))
                        }
                n || (n = {
                    no: t.err_no,
                    msg: t.err_msg || ""
                },
                delete i.err_no,
                delete i.err_msg,
                t = {
                    data: i,
                    errInfo: n
                })
            }
            return t
        }
        var a = function() {};
        t.prototype = {
            get_isComplete: function() {
                return this._isComplete
            },
            get_value: function() {
                if (!this._isComplete)
                    return void 0;
                if (this._exception)
                    throw this._exception;
                return this._value
            },
            call: function(e) {
                for (var t = [], n = 0, i = arguments.length - 1; i > n; n++)
                    t[n] = arguments[n + 1];
                return this.when(function(n) {
                    return n[e].apply(n, t)
                })
            },
            getValue: function(e) {
                return this.when(function(t) {
                    return t[e]
                })
            },
            setValue: function(e, t) {
                this.whenOnly(function(n) {
                    n[e] = t
                })
            },
            when: function(e, n, i) {
                return t.when(this, e, n, i)
            },
            whenOnly: function(e, n, i) {
                t.whenOnly(this, e, n, i)
            },
            success: function(e, t) {
                return this.when(e, a, t)
            },
            fail: function(e, t) {
                return this.when(a, e, t)
            },
            _enqueueOne: function(e) {
                this._isComplete ? this._notify(e) : this._requests.push(e)
            },
            _notify: function(e) {
                this._exception ? e.breakPromise && e.breakPromise(this._exception) : e.fulfillPromise && e.fulfillPromise(this._value)
            },
            _notifyAll: function() {
                for (var e = 0, t = this._requests.length; t > e; e++)
                    this._notify(this._requests[e])
            },
            _fulfillPromise: function(e) {
                this._value = e,
                this._exception = null,
                this._isComplete = !0,
                this._notifyAll()
            },
            _breakPromise: function(e) {
                this._value = null,
                this._exception = e || new Error("An error occured"),
                this._isComplete = !0,
                this._notifyAll()
            }
        },
        t.when = function(e, n, i, s) {
            return new t(function(o, r) {
                t.make(e)._enqueueOne({
                    fulfillPromise: function(e) {
                        o(n ? n.call(s, e) : e)
                    },
                    breakPromise: function(e) {
                        if (i)
                            try {
                                o(i.call(s, e))
                            } catch (t) {
                                r(t)
                            }
                        else
                            r(e)
                    }
                })
            }
            )
        }
        ,
        t.whenOnly = function(e, n, i, s) {
            t.make(e)._enqueueOne({
                fulfillPromise: function(e) {
                    n && n.call(s, e)
                },
                breakPromise: function(e) {
                    i && i.call(s, e)
                }
            })
        }
        ,
        t.make = function(e) {
            return e instanceof t ? e : t.immediate(e)
        }
        ,
        t.immediate = function(e) {
            return new t(function(t) {
                t(e)
            }
            )
        }
        ;
        var c = {};
        !function(e) {
            var t = new RegExp("(^[\\s\\t\\xa0\\u3000]+)|([\\u3000\\xa0\\s\\t]+$)","g");
            e.trim = function(e) {
                return String(e).replace(t, "")
            }
            ,
            e.getUniqueId = function(e) {
                return e + Math.floor(2147483648 * Math.random()).toString(36)
            }
            ,
            e.g = function(e) {
                return e ? "string" == typeof e || e instanceof String ? document.getElementById(e) : !e.nodeName || 1 != e.nodeType && 9 != e.nodeType ? null : e : null
            }
            ,
            e.getParent = function(t) {
                return t = e.g(t),
                t.parentElement || t.parentNode || null
            }
            ,
            e.encodeHTML = function(e) {
                return String(e).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;")
            }
            ,
            e.array = e.array || {},
            e.array.indexOf = function(e, t, n) {
                var i = e.length;
                for (n = 0 | n,
                0 > n && (n = Math.max(0, i + n)); i > n; n++)
                    if (n in e && e[n] === t)
                        return n;
                return -1
            }
            ,
            e.browser = e.browser || {},
            e.browser.opera = /opera(\/| )(\d+(\.\d+)?)(.+?(version\/(\d+(\.\d+)?)))?/i.test(navigator.userAgent) ? +(RegExp.$6 || RegExp.$2) : void 0,
            e.insertHTML = function(t, n, i) {
                t = e.g(t);
                var s, o;
                return t.insertAdjacentHTML && !e.browser.opera ? t.insertAdjacentHTML(n, i) : (s = t.ownerDocument.createRange(),
                n = n.toUpperCase(),
                "AFTERBEGIN" == n || "BEFOREEND" == n ? (s.selectNodeContents(t),
                s.collapse("AFTERBEGIN" == n)) : (o = "BEFOREBEGIN" == n,
                s[o ? "setStartBefore" : "setEndAfter"](t),
                s.collapse(o)),
                s.insertNode(s.createContextualFragment(i))),
                t
            }
        }(c),
        e.base = c;
        var l = {};
        !function(n) {
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
        var d = "https://passport.baidu.com"
          , u = {
            getApiInfo: "/v2/api/?getapi",
            getLoginHistory: "/v2/api/?loginhistory",
            loginCheck: "/v2/api/?logincheck",
            getVerifyCodeStr: "/v2/?reggetcodestr",
            getRegSmsVerifyCodeStr: "/v2/?regsmscodestr",
            checkUserName: "/v2/?regnamesugg",
            checkPassword: "/v2/?regpwdcheck",
            checkMail: "/v2/?regmailcheck",
            isUserNoName: "/v2/api/?ucenteradduname",
            checkPhone: "/v2/?regphonecheck",
            getphonestatus: "/v2/?getphonestatus",
            sendPhoneCode: "/v2/?regphonesend",
            multiBind: "/v2/?multiaccountassociate",
            multiUnbind: "/v2/?multiaccountdisassociate",
            multiCheckUserName: "/v2/?multiaccountusername",
            multiGetaccounts: "/v2/?multiaccountget",
            multiSwitchuser: "/v2/?loginswitch",
            checkVerifycode: "/v2/?checkvcode",
            getRsaKey: "/v2/getpublickey",
            authwidGetverify: "/v2/sapi/authwidgetverify",
            checkIDcard: "/v3/finance/main/idnumcert",
            checkIDcardSecondStep: "/v3/finance/main/upcert",
            checkIDcardAllStep: "/v3/finance/main/idnumcert",
            checkIDcardState: "/v3/finance/main/checkupcert"
        }
          , p = {
            login: "/v2/api/?login",
            reg: "/v2/api/?reg",
            fillUserName: "/v2/api/?ucenteradduname",
            regPhone: "/v2/api/?regphone",
            checkIDcard: "/v3/finance/main/idnumcert",
            checkIDcardSecondStep: "/v3/finance/main/upcert",
            checkIDcardAllStep: "/v3/finance/main/idnumcert"
        }
          , g = {
            getApiInfo: {
                apiType: "class"
            },
            login: {
                memberPass: "mem_pass",
                safeFlag: "safeflg",
                isPhone: "isPhone",
                timeSpan: "ppui_logintime",
                logLoginType: "logLoginType"
            },
            fillUserName: {
                selectedSuggestName: "pass_fillinusername_suggestuserradio",
                timeSpan: "ppui_fillusernametime"
            },
            reg: {
                password: "loginpass",
                timeSpan: "ppui_regtime",
                suggestIndex: "suggestIndex",
                suggestType: "suggestType",
                selectedSuggestName: "pass_reg_suggestuserradio_0",
                logRegType: "logRegType"
            },
            regPhone: {
                password: "loginpass",
                timeSpan: "ppui_regtime",
                suggestIndex: "suggestIndex",
                suggestType: "suggestType",
                selectedSuggestName: "pass_reg_suggestuserradio_0",
                logRegType: "logRegType"
            }
        }
          , h = {
            loginCheck: {
                isPhone: function(e) {
                    return e ? "true" : "false"
                }
            },
            login: {
                memberPass: function(e) {
                    return e ? "on" : ""
                }
            }
        }
          , f = {
            checkPassword: {
                fromreg: 1
            },
            reg: {
                registerType: 1,
                verifypass: function(e) {
                    return e.password
                }
            }
        }
          , m = {
            password: !0
        }
          , v = {
            login: function() {}
        }
          , b = {
            checkUserName: "reg",
            checkMail: "reg",
            checkPhone: "regPhone",
            sendPhoneCode: "regPhone",
            multiCheckUserName: "multiBind",
            multiSwitchuser: "changeUser",
            checkVerifycode: "checkVerifycode"
        }
          , y = passport.err.getCurrent().errMsg || passport.err.getCurrent()
          , E = {};
        e.setContext = function(e) {
            E.product = e.product || E.product,
            E.charset = e.charset || E.charset,
            E.staticPage = e.staticPage || E.staticPage,
            E.token = e.token || E.token,
            E.subpro = e.subpro || E.subpro
        }
        ,
        e.traceID = {
            headID: e.traceID && e.traceID.headID || "",
            flowID: e.traceID && e.traceID.flowID || "",
            cases: e.traceID && e.traceID.cases || "",
            initTraceID: function(e) {
                var t = this;
                e && e.length > 0 ? (t.headID = e.slice(0, 6),
                t.flowID = e.slice(6, 8)) : t.destory()
            },
            createTraceID: function() {
                var e = this;
                return e.headID + e.flowID + e.cases
            },
            startFlow: function(e) {
                var t = this
                  , n = t.getFlowID(e);
                0 === t.flowID.length || t.flowID === n ? (t.createHeadID(),
                t.flowID = n) : t.finishFlow(n)
            },
            finishFlow: function() {
                var e = this;
                e.destory()
            },
            getRandom: function() {
                return parseInt(90 * Math.random() + 10, 10)
            },
            createHeadID: function() {
                var e = this
                  , t = (new Date).getTime() + e.getRandom().toString()
                  , n = Number(t).toString(16)
                  , i = n.length
                  , s = n.slice(i - 6, i).toUpperCase();
                e.headID = s
            },
            getTraceID: function(e) {
                var t = this
                  , n = e && e.traceid || "";
                t.initTraceID(n)
            },
            getFlowID: function(e) {
                var t = {
                    login: "01",
                    reg: "02"
                };
                return t[e]
            },
            setData: function(e) {
                var t = this;
                return e.data ? e.data.traceid = t.createTraceID() : e.url = e.url + (e.url.indexOf("?") > -1 ? "&" : "?") + "traceid=" + t.createTraceID(),
                e
            },
            destory: function() {
                var e = this;
                e.headID = "",
                e.flowID = ""
            }
        };
        for (var _ in u)
            u.hasOwnProperty(_) && (e[_] = n(_, u[_]));
        for (var _ in p)
            p.hasOwnProperty(_) && (e[_] = n(_, p[_], !0));
        e.jsonp = function(e, t) {
            return 0 != e.indexOf("http") && (e = d + e),
            t = t || {},
            t.flag_code && 1 == t.flag_code || (t.apiver = "v3"),
            t.tt = (new Date).getTime(),
            l.jsonp(e, t, {
                charset: "utf-8",
                processData: function(e) {
                    return r(e)
                }
            })
        }
        ,
        e.post = function(e, t) {
            return t = t || {},
            e = "wap" == t.apitype ? e : d + e,
            t.staticpage = t.staticpage || E.staticPage,
            t.charset = t.charset || E.charset || document.characterSet || document.charset || "",
            t.token = t.token || E.token,
            t.tpl = t.tpl || E.product,
            l.submit(e, t, {
                charset: "utf-8",
                processData: function(e) {
                    return r(e)
                }
            })
        }
        ,
        e.request = l
    }(passport.data);
