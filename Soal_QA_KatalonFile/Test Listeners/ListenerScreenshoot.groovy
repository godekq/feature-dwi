import org.junit.rules.TestName

import com.kms.katalon.core.annotation.AfterTestCase
import com.kms.katalon.core.configuration.RunConfiguration
import com.kms.katalon.core.context.TestCaseContext
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile

import internal.GlobalVariable

class ListenerScreenshoot {
	/**
	 * Executes after every test case ends.
	 * @param testCaseContext related information of the executed test case.
	 */
	@AfterTestCase
	def sampleAfterTestCase(TestCaseContext testCaseContext) {
		println testCaseContext.getTestCaseId()
		println testCaseContext.getTestCaseStatus()
		
	def ssPath= RunConfiguration.getExecutionSourceName().toString()
		Mobile.takeScreenshot(GlobalVariable.ssPath+ssPath+TestName+'.png')
	}
}