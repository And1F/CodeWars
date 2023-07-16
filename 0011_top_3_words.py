from re import findall
def top_3_words(text):
    words = (findall(r"[A-Za-z][\w']*", text))
    words = sorted([x.lower() for x in words])
    words.append("+")
    counted = sorted([[words.count(words[x]), words[x]] for x in range(len(words)-1) if words[x] != words[x+1]])
    print(counted)
    try:
        return [counted[-1][1], counted[-2][1], counted[-3][1]]       
    except:
        try:
            return [counted[-1][1], counted[-2][1]]
        except:
            try:    
                return [counted[-1][1]]
            except:
                return []
print(top_3_words("PfjYhLTGwR?!ajQs- _,;jbC/!IXR:IXR_ .;?jbC:: ,dRFNisr-,!xNpt'ezv!!. ?dRFNisr, PfjYhLTGwR,.;?;dRFNisr.IXR_.?IXR_;xNpt'ezv?:xNpt'ezv?/:-ajQs :xNpt'ezv ,nckNfGCFQK.IXR :?/IXR_dRFNisr?,xNpt'ezv?!/jbC; PfjYhLTGwR:?/.?jbC-nckNfGCFQK-:.-PCDKzszL_xNpt'ezv : xNpt'ezv./_:!nckNfGCFQK??:GjzvPVzSis; ?jbC-,!nckNfGCFQK?xNpt'ezv!_;_!nckNfGCFQK/PfjYhLTGwR:!,ajQs!nckNfGCFQK dRFNisr!!/,:xNpt'ezv-/jbC,GjzvPVzSis_:PCDKzszL:?PfjYhLTGwR.., ?jbC:?,dRFNisr: . jbC!.:nckNfGCFQK.GjzvPVzSis.xNpt'ezv-:jbC!!/!xNpt'ezv  ,:IXR,;xNpt'ezv;;nckNfGCFQK:xNpt'ezv;__IXR. / GjzvPVzSis-,PfjYhLTGwR?,;,IXR_!ajQs .:GjzvPVzSis !?_IXR-.;dRFNisr nckNfGCFQK/; ,PfjYhLTGwR-dRFNisr!:;ajQs/. xNpt'ezv,:GjzvPVzSis_.?:!xNpt'ezv/..jbC//;GjzvPVzSis//.PfjYhLTGwR-:_;?jbC::.;IXR ;,:jbC-!?dRFNisr:PCDKzszL:--jbC  :,_PCDKzszL/nckNfGCFQK.,PfjYhLTGwR!?:/gGvAG;?ajQs :IXR;_jbC,-.;GjzvPVzSis;.:IXR-_.xNpt'ezv,IXR,- ajQs:,?/:xNpt'ezv -PfjYhLTGwR/!;;xNpt'ezv-!!.;nckNfGCFQK?,/;?xNpt'ezv :?;xNpt'ezv_!;xNpt'ezv;, xNpt'ezv-/ nckNfGCFQK;IXR!:jbC/-,_jbC IXR-;: .IXR:;/xNpt'ezv!_;jbC/__:!jbC,;IXR,.?. nckNfGCFQK ;-IXR._/IXR?xNpt'ezv!!:_.IXR._?.:PfjYhLTGwR:?GjzvPVzSis!-!xNpt'ezv .__.ajQs::dRFNisr?_xNpt'ezv/?!;IXR.-,.dRFNisr;-ajQs,?: /PCDKzszL;!;;xNpt'ezv:/xNpt'ezv?_!? IXR_//:"))