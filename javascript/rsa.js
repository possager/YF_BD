/**
 * Created by slience-pc on 2018/2/7.
 */

function a(e) {
            try {
                return Cn(this.getKey().encrypt(e))
            } catch (t) {
                return !1
            }
        }


function getkey(e) {
            if (!true) {/**这里边的值本来是this.key，因为this这个东西没法构造，反正也是1**/
                if (this.key = new Jn,
                e && "[object Function]" === {}.toString.call(e))
                    return void this.key.generateAsync(this.default_key_size, this.default_public_exponent, e);
                this.key.generate(this.default_key_size, this.default_public_exponent)
            }
            return this.key
        }


function encrypt(e) {
            var t = un(e, this.n.bitLength() + 7 >> 3);
            if (null == t)
                return null;
            var n = this.doPublic(t);
            if (null == n)
                return null;
            var i = n.toString(16);
            return 0 == (1 & i.length) ? i : "0" + i
        }

function y() {
            return this.t <= 0 ? 0 : this.DB * (this.t - 1) + b(this[this.t - 1] ^ this.s & this.DM)
        }