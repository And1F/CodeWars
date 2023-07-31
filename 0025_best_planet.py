import re
def best_planet(solar_system, max_size):
    required_elements = ['H', 'C', 'N', 'O', 'P', 'Ca']
    ans = [0,0]
    for planet in solar_system:
        size = int(planet[planet.index("_")+1:])
        elements = re.findall(r'[A-Z][a-z]*', planet)
        if all(item in elements for item in required_elements) and max_size >= size > ans[1]:
            ans = [solar_system[solar_system.index(planet)], size]
    return "" if ans[1] == 0 else ans[0]
solar_system  = ['OCdInHFlSnCZnCaP_142', 'CNdOSeIPBhBeNbLaBkCaTbFmCuCmHAcRaCoGaHeScReNRnClPa_93', 'LaPWAlDsHeErCuNePrNXeArORaGdBkInCrFSiCMtGeCaSrHoBeY_317', 'LuTiSnFmErNArNhZnCTcNeZrCuCaHfMgDsRaHDb_267', 'BhMgHTmMtBiHgLuBeGdSmArNaCaWTeNHfPmIrAsPRgOPdVAtUC_212', 'KFLrAlKrTeFlErYbBhCsCfThBrLaClBNdAtIWSbTmPbFmU_394', 'MdPdCPaClAmBhCdRaNpFePSmSrSnSbFrTlGaErHSiBCaLiNhPtO_345', 'PuTmZnRhNbPdRaRbFlLiNhBhAuBaIrHsCaSgGeCmLuMtBiCeInPaSrOLa_364', 'HNdAtUMnLrSeKrNGeBGdSgOAl_121', 'SrBiTcPCsICCmRuCrFeRaLiBaHHsTlMoCaCl_127', 'NdClZrOgXeMtCeGeTlSCsAmTeRnMoPtCmLrSrBaITaSeHeErDy_391', 'PNoHBaAtPaFrSgBeAgFeDsPrPdCaNCO_288', 'FmEsHRgSCmWLrCrTmNeOArLiTlNaPTiGdYbCaNpCNPmPo_343', 'AmTmFrIZrHNhCHoSCaAcTbClKPrNInP_108', 'OsFeTiSgHSiCRbBPInLrCaWAlBeONCo_470', 'RnCfBiDsYbEsRbBAlSiHMtCMoCn_369', 'CKCaGeHPDsOEuNOsPu_484', 'NNbBeCaBaPtRbTeLuThPdCdBkMtSiOAtPa_161', 'PtPDbArFCaSrCSgPaErNPbAmEsInLuCsOIHHsNhNpRbBhSnRn_468', 'PtOCaHNaNHfCPaTmErP_422', 'AmDbKCdTcPuThEsCeLiNeNiNoHsDy_84', 'PmNbCaRbHCsTiPYbBkCdNhRu_261', 'NpAmCnNhVSrCThKrZrScYSeMtSbNKTsMdPBiRbDbCdMoBkHHgAs_228', 'BiCCaRuCsPaPTmKrMcAr_100', 'BeHCoHePdPbCPNCaNiEs_79', 'HfCDsDyPMoBkNbHPbON_407', 'VTsSeKBhRbNoPmCOSrCfCaCmF_342', 'TlNRgAlSbRuNaNdFrCs_144', 'NRhCOCmPCaIHHeTc_33', 'ErGeNNaHCaYMdDbBeSbLrEsCO_466', 'ScNTmNeCaHCLaPTbONpBk_190']
limit = 392
print(best_planet(solar_system, limit), "+ans")