
function f(b, a) {
            for (var c = 0; c < a.length; c++) b.push(a[c]);
            return b
        }

        function g(b, a) {
            for (var c = 0; c < b.length; c++) a(b[c], c)
        }

        function l(b, a, c) {
            void 0 === c && (c = null);
            for (var d = [], e = 0; e < b.length; e++) d.push(a.apply(c, [b[e], e]));
            return d
        }

        function m(b) {
            return "[object Array]" === Object.prototype.toString.call(b)
        }
        var n = function () {
                function b() {}
                b.B = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/<$+-%>{:* \\,}[^=_~&](")';
                return b
            }(),
            r = function () {
                function b(a) {
                    this.m = [];
                    this.w = 0;
                    this.D = [];
                    var c = this;
                    this.g = a;
                    this.g.i._A = function (a) {
                        c.w = a
                    };
                    this.m.push(this.g)
                }
                b.prototype.va = function () {
                    return function c(d, e) {
                        return e ? c(d ^ e, (d & e) << 1) : d
                    }(8, 2)
                };
                b.prototype.K = function (a, c) {
                    void 0 === c && (c = -1);
                    this.m.push(a);
                    this.g = this.m[this.m.length - 1]; - 1 !== c && (this.w = c);
                    this.D.push(this.w)
                };
                b.prototype.oa = function (a) {
                    var c = this;
                    g(a[1], function (a) {
                        return c.b(a)
                    })
                };
                b.prototype.pa = function (a) {
                    a[2] ? this.b(a[2]) : this.f(void 0);
                    this.g.i[l(function d(a) {
                        return m(a) ? [].concat.apply([], l(a, d)) : a
                    }(a[1]), this.o, this).join("")] = this.h()
                };
                b.prototype.W = function (a) {
                    this.b(a[1]);
                    this.h() ? this.b(a[2]) : this.b(a[3])
                };
                b.prototype.aa = function (a) {
                    var c = this;
                    this.g.i[l(function e(a) {
                        return m(a) ? [].concat.apply([], l(a, e)) : a
                    }(a[1]), this.o, this).join("")] = new p(this, this.g, l(a[2], function (a) {
                        return c.C(a[1])
                    }), a[3], a[4])
                };
                b.prototype.ea = function (a) {
                    -2 === a[1] ? this.f(new RegExp(this.C(a[2]), this.C(a[3]))) : -1 === a[1] ? this.f(a[2]) : this.f(a[1])
                };
                b.prototype.ca = function (a, c) {
                    var d = this.g.G(l(function k(a) {
                        return m(a) ? [].concat.apply([], l(a, k)) : a
                    }(a[1]), this.o, this).join(""));
                    if (void 0 !== d) c ? this.f(d) : this.f(d.j[d.s]);
                    else throw Error();
                };
                b.prototype.T = function (a) {
                    var c = this;
                    this.b(a[1]);
                    this.b(a[2]);
                    var d = this.h(),
                        e = this.h();
                    [
                        function () {
                            c.f(d + e)
                        },
                        function () {
                            c.f(d - e)
                        },
                        function () {
                            c.f(d / e)
                        },
                        function () {
                            c.f(d < e)
                        },
                        function () {
                            c.f(d > e)
                        },
                        function () {
                            c.f(d <= e)
                        },
                        function () {
                            c.f(d >= e)
                        },
                        function () {
                            c.f(d == e)
                        },
                        function () {
                            c.f(d % e)
                        },
                        function () {
                            c.f(d ^ e)
                        },
                        function () {
                            c.f(d * e)
                        },
                        function () {
                            c.f(d === e)
                        },
                        function () {
                            c.f(d !== e)
                        },
                        function () {
                            c.f(d << e)
                        },
                        function () {
                            c.f(d | e)
                        },
                        function () {
                            c.f(d >> e)
                        },
                        function () {
                            c.f(d & e)
                        }
                    ][a[3]]()
                };
                b.prototype.f = function (a) {
                    this.g.xa(a)
                };
                b.prototype.P = function (a) {
                    var c = this;
                    try {
                        g(a, function (a) {
                            return c.b(a)
                        }), this.status = 0
                    } catch (d) {
                        this.status = 1
                    } finally {
                        this.g = null, this.m = []
                    }
                };
                b.prototype.ba = function (a) {
                    var c = this;
                    this.f(new p(this, this.g, l(a[1], function (a) {
                        return c.C(a[1])
                    }), a[2], a[3]))
                };
                b.prototype.J = function (a) {
                    var c = this;
                    g(a[2], function (a) {
                        return c.b(a)
                    });
                    this.b(a[1], !0);
                    var d = this.h(),
                        e = d.j,
                        d = d.j[d.s],
                        b = [];
                    for (a = a[2].length; a--;) b.unshift(this.h());
                    if (d.apply) e = d.apply(e, b), this.f(e);
                    else throw Error();
                };
                b.prototype.C = function (a) {
                    return l(function d(a) {
                        return m(a) ? [].concat.apply([], l(a, d)) : a
                    }(a), this.o, this).join("")
                };
                b.prototype.S = function (a) {
                    this.b(a[2]);
                    this.b(a[3], !0);
                    this.b(a[3]);
                    var c = this.h(),
                        d = this.h(),
                        b = this.h();
                    [
                        function () {},
                        function () {
                            b = c + b
                        },
                        function () {
                            b = c - b
                        }
                    ][a[1]]();
                    d.j ? d.j[d.s] = b : this.g.i[d] = b
                };
                b.prototype.o = function (a) {
                    a ^= this.w;
                    return n.B[0 <= a && 26 >= a || 64 < a ? a : 32 <= a && 58 >= a ? 26 + a - 32 : -17 <= a && -8 >= a ? 52 + a + 17 : 0]
                };
                b.prototype.M = function () {
                    this.m.pop();
                    this.D.pop();
                    this.g = this.m[this.m.length - 1];
                    this.w = this.D[this.D.length - 1]
                };
                b.prototype.h = function () {
                    return this.g.O()
                };
                b.prototype.fa = function (a) {
                    this.b(a[2]);
                    var c = this.h(),
                        d = this;
                    [
                        function () {
                            c ? d.f(c) : d.b(a[3])
                        },
                        function () {
                            d.b(a[3]);
                            d.f(c && d.h())
                        }
                    ][a[1]]()
                };
                b.prototype.qa = function () {
                    return [this.oa, this.pa, this.aa, this.ea, this.ca, this.T, this.ba]
                };
                b.prototype.R = function (a) {
                    var c = this;
                    g(a[1], function (a) {
                        return c.b(a)
                    });
                    var d = [];
                    for (a = a[1].length; a--;) d.unshift(this.h());
                    this.f(d)
                };
                b.prototype.ha = function (a) {
                    var c = this,
                        d = {};
                    g(a[1], function (a) {
                        c.b(a[1]);
                        d[l(function h(a) {
                            return m(a) ? [].concat.apply([], l(a, h)) : a
                        }(a[0]), c.o, c).join("")] = c.h()
                    });
                    this.f(d)
                };
                b.prototype.ja = function () {
                    this.f(this.g.i["this"] || this.g.i)
                };
                b.prototype.ga = function (a, c) {
                    var d;
                    if (1 === a[1])
                        if (d = this.g.G(l(function h(a) {
                            return m(a) ? [].concat.apply([], l(a, h)) : a
                        }(a[4][1]), this.o, this).join(""))) d = d.j[d.s];
                        else throw Error();
                    else this.b(a[4], !1), d = this.h(); if (void 0 !== d) {
                        0 === a[3] && 1 === a[2] ? this.f(l(function h(a) {
                            return m(a) ? [].concat.apply([], l(a, h)) : a
                        }(a[5][1]), this.o, this).join("")) : this.b(a[5]);
                        var b = this.h();
                        c ? this.f(this.g.ta(d, b)) : this.f(d[b])
                    } else throw Error();
                };
                b.prototype.na = function (a) {
                    this.b(a[1], !0);
                    var c = this.h(),
                        d = c.j[c.s];
                    [
                        function () {
                            d++
                        },
                        function () {
                            d--
                        }
                    ][a[2]]();
                    c.j[c.s] = d
                };
                b.prototype.sa = function () {
                    return [this.$, this.da, this.V, this.X, this.ka, this.la, this.Y]
                };
                b.prototype.b = function (a, c) {
                    void 0 === c && (c = !1);
                    if (!this.g.L && !this.g.u && !this.g.v) {
                        var d = f(this.qa(), f(this.ra(), f(this.sa(), [this.ia, this.fa, this.ma, this.W, this.U, this.Z]))),
                            b = a[0] - 3 * this.va() ^ this.w;
                        if (d[b]) d[b].apply(this, [a, c]);
                        else throw Error();
                    }
                };
                b.prototype.Z = function (a) {
                    var c = this;
                    this.b(a[1], !0);
                    var d = this.h();
                    this.b(a[2]);
                    for (var b in this.h()) {
                        d.j[d.s] = b;
                        g(a[3], function (a) {
                            return c.b(a)
                        });
                        if (this.g.u) {
                            this.g.u = !1;
                            break
                        }
                        this.g.v && (this.g.v = !1)
                    }
                };
                b.prototype.$ = function (a) {
                    var c = this;
                    this.b(a[1]);
                    do {
                        g(a[2], function (a) {
                            return c.b(a)
                        });
                        if (this.g.u) {
                            this.g.u = !1;
                            break
                        }
                        this.g.v && (this.g.v = !1);
                        this.b(a[3]);
                        this.b(a[4]);
                        if (!this.h()) break
                    } while (1)
                };
                b.prototype.U = function (a) {
                    var c = this;
                    g(a[1], function (a) {
                        return c.b(a)
                    })
                };
                b.prototype.da = function (a) {
                    this.b(a[1]);
                    this.h() ? a[2] && this.b(a[2]) : a[3] && this.b(a[3])
                };
                b.prototype.V = function () {
                    this.g.u = !0
                };
                b.prototype.X = function () {
                    this.g.v = !0
                };
                b.prototype.ma = function (a) {
                    var c = this;
                    this.b(a[2], !1);
                    var d = this.h();
                    [
                        function () {
                            c.f(!d)
                        },
                        function () {
                            c.f(-d)
                        }
                    ][a[1]]()
                };
                b.prototype.ra = function () {
                    return [this.J, this.J, this.S, this.R, this.ha, this.ja, this.ga, this.na]
                };
                b.prototype.ka = function (a) {
                    this.b(a[1]);
                    throw this.h();
                };
                b.prototype.la = function (a) {
                    var c = this;
                    try {
                        g(a[1], function (a) {
                            return c.b(a)
                        })
                    } catch (e) {
                        var d = new q;
                        d.A = this.g;
                        this.K(d);
                        a[2] && (this.g.i[l(function h(a) {
                            return m(a) ? [].concat.apply([], l(a, h)) : a
                        }(a[2][1]), this.o, this).join("")] = e);
                        g(a[3], function (a) {
                            return c.b(a)
                        });
                        this.M()
                    } finally {
                        a[4] && g(a[4], function (a) {
                            return c.b(a)
                        })
                    }
                };
                b.prototype.Y = function (a) {
                    this.b(a[1])
                };
                b.prototype.ia = function (a) {
                    a[1] && this.b(a[1]);
                    this.g.L = !0
                };
                return b
            }(),
            q = function () {
                function b(a) {
                    this.F = function () {
                        return function (a, d) {
                            this.j = a;
                            this.s = d
                        }
                    }();
                    this.v = this.u = this.L = !1;
                    this.H = [];
                    this.i = a || {
                        btoa: function (a, d, b, k, h) {
                            void 0 === d && (d = n.B.slice(0, 64));
                            for (k = h = ""; a[k | 0] || (d = "=", k % 1); h += d[63 & b >> 8 - k % 1 * 8]) b = b << 8 | a.charCodeAt(k -= -.75);
                            return h
                        }
                    }
                }
                b.prototype.O = function () {
                    return this.H.pop()
                };
                b.prototype.xa = function (a) {
                    this.H.push(a)
                };
                b.prototype.ta = function (a, c) {
                    return new this.F(a, c)
                };
                b.prototype.G = function (a) {
                    if (this.i.hasOwnProperty(a)) return new this.F(this.i, a);
                    if (this.A) return this.A.G(a);
                    if (global[a]) return new this.F(global, a)
                };
                return b
            }(),
            p = function () {
                function b(a, c, d, b, k) {
                    this.I = a;
                    this.ua = b;
                    this.A = c;
                    this.N = d;
                    this.wa = k
                }
                b.prototype.apply = function (a, c) {
                    var b = this,
                        e = new q;
                    e.A = this.A;
                    this.N && g(this.N, function (a, b) {
                        e.i[a] = c[b]
                    });
                    e.i["this"] = a;
                    this.I.K(e, this.wa);
                    try {
                        g(this.ua, function (a) {
                            return b.I.b(a, !1)
                        })
                    } finally {
                        this.I.M()
                    }
                    if (0 !== e.H.length) return e.O()
                };
                return b
            }(),
            t = {};
        // global._BSK = {
        //     a: function (b, a) {
        //         a.MAP = n.B;
        //         (new r(new q(a))).P(t[b])
        //         return a;
        //
        //     }, c: function (b, a) {
        //         b.MAP = n.B;
        //         (new r(new q(b))).P(a)
        //     }, l: function (b, a) {
        //         t[b] = a
        //     }
        // };
        b1=b;
        a1=a;
        function a2(b, a) {
                a.MAP = n.B;
                (new r(new q(a))).P(t[b])
                return a.OUT;}

        return a2(b1,a1);