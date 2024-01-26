import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

Mobile.startExistingApplication('com.tokopedia.tkpd')

WebUI.delay(10)

Mobile.tap(findTestObject('Object Repository/Select Pulsa dan Tagihan'), 0)

WebUI.delay(10)

Mobile.tap(findTestObject('Object Repository/Select Pulsa'), 0)

WebUI.delay(10)

Mobile.setText(findTestObject('Additional/InputNomor'), InputNumber, 0)

WebUI.delay(10)

Mobile.tap(findTestObject('Object Repository/Select nominal 15.000'), 0)

Mobile.tap(findTestObject('Object Repository/btn.Lanjutkan'), 0)

WebUI.delay(10)

Mobile.tap(findTestObject('Object Repository/Pilih Pembayaran'), 0)

WebUI.delay(10)

Mobile.verifyElementText(findTestObject('Object Repository/text Pakai GoPay Tabungan'), 'Pakai GoPay Tabungan')

Mobile.tap(findTestObject('Object Repository/btn.Bayar'), 0)

Mobile.closeApplication()

