/**
 * Created by slience-pc on 2018/2/7.
 */

_submitSmsForm: function() {
            function e() {
                t._postSmsData(o)
            }
            var t = this
              , n = document.getElementById(t.$getId("smsPhone"))
              , i = document.getElementById(t.$getId("smsVerifyCode"));
            if (!t._validatorPhoneFn(n))
                return void n.focus();
            if (t._validatorSmsFn(i)) {
                var s = t.fireEvent("beforeSubmit");
                if (s) {
                    t.getElement("smsSubmit").style.color = "#9ebef4";
                    var o = baidu.form.json(t.getElement("smsForm"));
                    o.password = t._SBCtoDBC(o.password),
                    o.username = t._SBCtoDBC(o.username),
                    o.FP_UID = t._getCookie("FP_UID") || "",
                    o.FP_INFO = window.PP_FP_INFO || "",
                    t.loginConnect({
                        username: o.username,
                        password: o.password,
                        countrycode: t.getElement("smsPhoneCountryLabel") ? baidu(t.getElement("smsPhoneCountryLabel")).attr("data-countrycode") || "" : "",
                        smsVcode: o.password,
                        isdpass: 1,
                        sms: 1
                    }, {
                        fail: function(e) {
                            t._setSmsGeneralError(e)
                        }
                    }, e)
                }
            }
        },