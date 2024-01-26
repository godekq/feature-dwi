import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

Mobile.startExistingApplication('com.tokopedia.tkpd')

Mobile.tap(findTestObject('Select Pulsa dan Tagihan'), 0)

Mobile.tap(findTestObject('Object Repository/Select Paket Data'), 0)

Mobile.setText(findTestObject('Additional/Set number in paket data'), InputNumber, 0)

Mobile.hideKeyboard()

Mobile.tap(findTestObject('Object Repository/Select filter 1-5GB'), 0)

Mobile.tap(findTestObject('Object Repository/Select Paket Data 1gb'), 0)

Mobile.tap(findTestObject('Object Repository/button Lanjutkan'), 0)

Mobile.tap(findTestObject('Object Repository/button Pilih Pembayaran'), 0)

Mobile.tap(findTestObject('Object Repository/Lihat semua metode bayar'), 0)

Mobile.tap(findTestObject('Object Repository/select BCA Virtual Account'), 0)

Mobile.tap(findTestObject('Object Repository/button bayar'), 0)

Mobile.verifyElementText(findTestObject('Object Repository/text BCA Virtual Account'), 'BCA Virtual Account')

Mobile.closeApplication()

