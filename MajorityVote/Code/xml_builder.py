import string
from string import Template
from data import *


class Xml:
    def __init__(self, data, columns, prefix):
        self.data = data
        self.columns = columns
        self.prefix = prefix

    def xml_builder(self):
        template = '''<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
           <HTMLContent>
               <![CDATA[
        <!-- YOUR HTML BEGINS -->
        <!DOCTYPE html>
        <html>
        <head>
        <meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>
                <script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
                </head>
        <crowd-form answer-format="flatten-objects">

            <p> <strong>Instructions: </strong> Please look at the images below closely and answer this question with 
            "yes" or "no". Make sure you scroll down to the end of page and select an answer before submitting. </p> 
            <p style="text-align:center;"> <b>Is there a <strong>${variable}</strong> in this set of images?</b> </p> 

            <!-- Your image file URLs will be substituted for the "image_url" variable below
                  when you publish a batch with a CSV input file containing multiple image file URLs.
                  To preview the element with an example image, try setting the src attribute to
                  "https://s3.amazonaws.com/cv-demo-images/basketball-outdoor.jpg" -->
            ${urls}
            <br><br>
                <div class="text-align:center;padding:300px;" style="width:200px; margin:auto;">
                  <input type="radio" id="yes" name="gender" value="yes" required>
                  <label for="yes">Yes</label>
                  <input type="radio" id="no" name="gender" value="no">
                  <label for="no">No</label>
                </div><br>
        </crowd-form>
        </html>
        <!-- YOUR HTML ENDS -->
        ]]>
           </HTMLContent>
           <FrameHeight>0</FrameHeight>
        </HTMLQuestion>'''
        xml_template = string.Template(template)
        variable = 'female'
        u = '<p style="text-align:center;">'
        i = 0
        urls = self.url_builder()
        for url in urls:
            if i % self.columns != 0 or i == 0:
                u += '<img src="' + url + '" style="max-width: 100%; max-height: 250px" />\n'
                if (i + 1) % self.columns == 0:
                    u += '</p>'
            else:
                u += '<p style="text-align:center;"><img src="' + url + '" style="max-width: 100%; max-height: 250px" /> \n'
            i += 1
        xml = xml_template.substitute(variable=variable, urls=u)
        #print(xml)

        with open("hit.xml", "w") as file:
            file.write(xml)
            # <p><img src="${url}" style="max-width: 100%; max-height: 250px" /></p>

    def url_builder(self):
        urls = []
        for img in self.data:
            str = self.prefix+img
            urls.append(str)
        return urls


#test

# data = Data('img2.csv').dataset_init()
# x = Xml(data[0:15], 5, 'https://cov-img.s3.amazonaws.com/feret-db/')
# x.xml_builder()