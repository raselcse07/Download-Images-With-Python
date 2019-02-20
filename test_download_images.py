from download_images import main



# Test the main function. Output will
# be True if the desired file exists
# otherwise output will be False. 
def test_main():
    assert main("Testcase/images.txt") == True
    assert main("Testcase/images2.txt") == True
    assert main("Testcase/images3.txt") == True

