import os
import re
import json
import shutil
from shutil import copyfile


class ModuleCheckProject:
    envPath = "C:\\liferay_workspace\\angular-pyton-tools\\test-tool\\tmp_projects\\Angular6Project"

    def __init__(self):
        consoleManager(1, "Initialization")
        self.getPath()
        self.checkPathEnvoirment()
        self.checkAngularVersion()
        self.checkProjectStructure()
        conf = self.checkConfiguration()
        ModuleUpdateProject(self.envPath, conf)

    def checkConfiguration(self):
        if os.path.isfile(self.envPath+"config-migr.json"):
            file = open(self.envPath + "config-migr.json", "r")
            packText = file.read()
            confJson = json.loads(packText)
            return confJson
        return ""

    def getPath(self):
        self.envPath = input("Enter the Angular project path: ")
        if self.envPath == "":
            self.envPath = "C:\\liferay_workspace\\angular-pyton-tools\\test-tool\\tmp_projects\\question-project"

    def checkPathEnvoirment(self):
        self.envPath = self.envPath.replace("\\", "/")
        valid = os.path.isdir(self.envPath)
        if not valid:
            exitError(1, self.envPath)
        if self.envPath[self.envPath.__len__() - 1] != '/':
            self.envPath += '/'
        packagePath = self.envPath
        packagePath += "package.json"
        consoleManager(1, packagePath)
        valid = os.path.isfile(packagePath)
        if not valid:
            exitError(1, packagePath)

    def checkAngularVersion(self):
        consoleManager(1, "Npm version:", 1)
        os.chdir(self.envPath)
        myCmd = 'npm -v'
        os.system(myCmd)
        consoleManager(1, "Angular version:", 1)
        # Check angular version
        packagePath = self.envPath
        packagePath += "package.json"
        file = open(packagePath, "r")
        packText = file.read()
        out = re.search("(\"@angular\\/cli\":[.]*.+\"*[0-9]\")", packText)
        str1 = out.group()
        out = re.search("[0-9.]+", str1)
        str2 = out.group()
        consoleManager(1, str2)
        if str2[0] != "6":
            exitError(2, "Angular version not valid")

    def checkProjectStructure(self):
        consoleManager(1, "Analizing project structure", 1)

        path = self.envPath + "tsconfig.json"
        checkFile(path)

        path = self.envPath + "angular.json"
        checkFile(path)

        path = self.envPath + "node_modules"
        checkDir(path)

        path = self.envPath + "src/app"
        checkDir(path)

        path = self.envPath + "src/assets"
        checkDir(path)

        path = self.envPath + "src/environments"
        checkDir(path)

        path = self.envPath + "src/styles.css"
        checkFile(path)

        path = self.envPath + "src/main.ts"
        checkFile(path)

        path = self.envPath + "src/polyfills.ts"
        checkFile(path)


# TODO rimuovere features
class ModuleUpdateProject:
    envPath = ""
    appName = ""

    configurated = False
    configuration = {}

    def __init__(self, envPath, jsonConfig):
        if jsonConfig != "":
            self.configurated = True
        else:
            jsonConfig = {}
        self.configuration = jsonConfig
        consoleManager(1, "Updating project structure", 1)
        self.envPath = envPath
        self.updateStructure()
        consoleManager(1, "Elaborating components", 1)
        self.elaborateComponentsApp()
        self.saveConfiguration()

    def saveConfiguration(self):
        npmBuildRcFile = open(self.envPath + "config-migr.json", "w")
        npmBuildRcFile.write(json.dumps(self.configuration))
        npmBuildRcFile.close()

    def updateStructure(self):
        consoleManager(1, "Updating package.json")
        file = open(self.envPath + "package.json", "r")
        packText = file.read()
        file.close()
        packJson = json.loads(packText)
        self.appName = packJson["name"]
        if not self.configurated:
            descriptionImp = input("Enter project description: ")
            self.configuration["project_description"] = descriptionImp
        else:
            descriptionImp = self.configuration["project_description"]
        packJson["description"] = descriptionImp
        consoleManager(1, "Description added")
        packJson["scripts"]["ng-start"] = packJson["scripts"]["start"]
        packJson["scripts"]["ng-build"] = packJson["scripts"]["build"]
        packJson["scripts"]["start"] = "lnbs-start"
        packJson["scripts"]["deploy"] = "npm run build && lnbs-deploy"
        packJson["scripts"]["translate"] = "lnbs-translate"
        packJson["scripts"]["copy-assets"] = "lnbs-copy-assets"
        packJson["scripts"]["build"] = "tsc && npm run copy-assets && liferay-npm-bundler"
        consoleManager(1, "Scripts added")
        consoleManager(1, "Portlet settings")
        if not self.configurated:
            inputText = input("Enter project category: ")
            self.configuration["project_category"] = inputText
        else:
            inputText = self.configuration["project_category"]
        portletJson = json.loads("{}")
        packJson["portlet"] = portletJson
        if not self.configurated:
            packJson["portlet"]["com.liferay.portlet.display-category"] = inputText
            inputText = input("Enter project css build path [/css/styles.css]: ")
            if inputText == "":
                inputText = "/css/styles.css"
            self.configuration["css_path"] = inputText
        else:
            inputText = self.configuration["css_path"]
        packJson["portlet"]["com.liferay.portlet.header-portlet-css"] = inputText
        if not self.configurated:
            inputText = input("Instanceable? type true or false [true]: ")
            if inputText == "":
                inputText = "true"
            self.configuration["istanceable"] = inputText
        else:
            inputText = self.configuration["istanceable"]
        instanceable = True
        if inputText != "true":
            instanceable = False
        packJson["portlet"]["com.liferay.portlet.instanceable"] = instanceable
        if not self.configurated:
            inputText = input("Enter portlet name: ")
            self.configuration["portlet_name"] = inputText
        else:
            inputText = self.configuration["portlet_name"]
        packJson["portlet"]["javax.portlet.name"] = inputText
        packJson["portlet"]["javax.portlet.security-role-ref"] = "power-user,user"
        packJson["portlet"]["javax.portlet.resource-bundle"] = "content.Language"
        consoleManager(1, "Portlet settings added")
        packJson["main"] = "index.js"
        consoleManager(1, "Added index.js as main", 1)
        file = open(self.envPath + "package.json", "w")
        file.write(json.dumps(packJson))
        file.close()
        consoleManager(1, "package.json updated correctly")

        consoleManager(1, "Updating tsconfig.json", 1)
        file = open(self.envPath + "tsconfig.json", "r")
        tsText = file.read()
        file.close()
        tsJson = json.loads(tsText)
        compilerOptions = tsJson["compilerOptions"]
        compilerOptions["outDir"] = "build"
        compilerOptions["emitDecoratorMetadata"] = True
        compilerOptions["experimentalDecorators"] = True
        compilerOptions["inlineSources"] = True
        libs = ['es2017', 'dom']
        compilerOptions["lib"] = libs
        compilerOptions["module"] = "commonjs"
        compilerOptions["moduleResolution"] = "node"
        compilerOptions["noImplicitAny"] = True
        compilerOptions["noStrictGenericChecks"] = True
        compilerOptions["sourceMap"] = True
        compilerOptions["suppressImplicitAnyIndexErrors"] = True
        compilerOptions["target"] = "es5"
        compilerOptions["typeRoots"] = ['./node_modules/@types/']
        tsJson["compilerOptions"] = compilerOptions
        tsJson["include"] = ['./src/**/*.ts']
        file = open(self.envPath + "tsconfig.json", "w")
        file.write(json.dumps(tsJson))
        file.close()
        consoleManager(1, "tsconfig.json updated correctly")

        consoleManager(1, "Generating sources", 1)
        consoleManager(1, "Generating .npmbuildrc")
        npmBuildRc = json.loads("{}")
        npmBuildRc["translatorTextKey"] = ""
        npmBuildRc["supportedLocales"] = []
        if not self.configurated:
            inputText = input("Insert your bundle workspace path [.../bundles]")
            if inputText == "":
                inputText = "C:\\liferay_workspace\\Bundles-work\\Bundle_1\\Workspace\\bundles"
            inputText.replace("/", "\\")
            self.configuration["bundle_workspace"] = inputText
        else:
            inputText = self.configuration["bundle_workspace"]
        npmBuildRc["liferayDir"] = inputText
        npmBuildRc["webpack"] = {
            "rules": [
                {
                    "test": "src\\\\.*\\.ts$",
                    "use": "ts-loader"
                }
            ],
            "extensions": [
                ".ts",
                ".js"
            ],
            "mainModule": "index.ts"
        }
        npmBuildRcFile = open(self.envPath + ".npmbuildrc", "w")
        npmBuildRcFile.write(json.dumps(npmBuildRc))
        npmBuildRcFile.close()
        consoleManager(1, ".npmbuildrc created correctly")

        consoleManager(1, "Generating .npmbundlerrc", 1)
        npmBundlerRc = json.loads("{}")
        npmBundlerRc["create-jar"] = {
            "output-dir": "dist",
            "features": {
                "js-extender": True,
                "web-context": "/" + self.appName,
                "localization": "features/localization/Language",
                "configuration": "features/configuration.json"
            }
        }
        npmBundlerRc["dump-report"] = True
        npmBundlerRc["process-serially"] = True
        npmBundlerRcFile = open(self.envPath + ".npmbundlerrc", "w")
        npmBundlerRcFile.write(json.dumps(npmBundlerRc))
        npmBundlerRcFile.close()
        consoleManager(1, ".npmbundlerrc created correctly")

        consoleManager(1, "Generating .npmignore", 1)
        npmIgnore = open(self.envPath + ".npmignore", "w")
        npmIgnore.write(".npmbuildrc")
        npmIgnore.close()
        consoleManager(1, ".npmignore created correctly")

        consoleManager(1, "Generating index page", 1)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file = open(dir_path + "/index.ts", "r")
        text = file.read()
        file = open(self.envPath + "src/index.ts", "w")
        file.write(text)
        file.close()
        consoleManager(1, "index.ts generated correctly")

        consoleManager(1, "Configuring app bootstrap module", 1)
        consoleManager(2, "Your app.module.ts will be updated")
        if not self.configurated:
            cont = input("continue? [Y/N]")
            if cont != "Y" and cont != "y":
                exit(4)
            consoleManager(2, "Please remove ALL from your Bootstrap", 1)
            cont = input("Have you done it? [Y/N]")
            if cont != "Y" and cont != "y":
                exit(4)
        checkFile(self.envPath + "src/app/app.module.ts")
        file = open(self.envPath + "src/app/app.module.ts", "r")
        text = file.read()
        file.close()
        declaration = self.getNgModuleStartCloseDeclaration(text)
        declarationReb = "({\n"
        if declaration.find("entryComponents") == -1:
            declarationReb += "entryComponents: [AppComponent],\n"
        declarationReb += declaration + "\n})\n"
        text = self.rebuildNgModuleDeclaration(text, declarationReb)
        if text.find("ngDoBootstrap()") == -1:
            moduleClassEnd = re.search("export class AppModule[ ]*{", text).end()
            textReb = text[:moduleClassEnd] + "\nngDoBootstrap() {}\n" + text[moduleClassEnd + 1:]
        else:
            textReb = text
        file = open(self.envPath + "src/app/app.module.ts", "w")
        file.write(textReb)
        file.close()
        consoleManager(1, "app.module.ts updated correctly")

        consoleManager(1, "Generating dynamic.loader.ts", 1)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file = open(dir_path + "/dynamic.loader.ts", "r")
        text = file.read()
        file = open(self.envPath + "src/app/dynamic.loader.ts", "w")
        file.write(text)
        file.close()
        consoleManager(1, "dynamic.loader.ts generated correctly")

        consoleManager(1, "Generating liferay types", 1)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file = open(dir_path + "/LiferayParams.ts", "r")
        text = file.read()
        path = self.envPath + "src/types"
        if not dirExist(path):
            os.makedirs(path)
        file = open(self.envPath + "src/types/LiferayParams.ts", "w")
        file.write(text)
        file.close()
        consoleManager(1, "LiferayParams generated correctly")

        consoleManager(1, "Generating assets dir", 1)
        path = self.envPath + "assets"
        if dirExist(path):
            shutil.rmtree(path, ignore_errors=True)
        try:
            os.makedirs(path)
        except:
            consoleManager(3, 'dir already exist')
        consoleManager(1, path)
        path = self.envPath + "assets/css"
        if not dirExist(path):
            os.makedirs(path)
        consoleManager(1, path)
        path = self.envPath + "assets/app"
        if not dirExist(path):
            try:
                os.makedirs(path)
            except:
                consoleManager(3, 'dir already exist')
        consoleManager(1, path)

        consoleManager(1, "Generating styles.css output", 1)
        file = open(self.envPath + "src/styles.css", "r")
        text = file.read()
        file = open(self.envPath + "assets/css/styles.css", "w")
        file.write(text)
        file.close()
        consoleManager(1, "styles.css generated correctly")

        consoleManager(1, "Migrating assets dir", 1)
        path = self.envPath + "src/assets"
        self.copytree(path, self.envPath + "assets")
        consoleManager(1, "Assets migrated correctly")

    def elaborateComponentsApp(self):
        path = self.envPath + "src/app"
        files = []
        for r, d, f in os.walk(path):
            r = r.replace("\\", "/")
            fis = {"files": f, "dir": str(r), "dirname": d}
            files.append(fis)
        for file in files:
            # Controllo se la directory esiste
            dir = file["dir"]
            directoryName = file["dirname"]
            if dir.find(self.envPath) == 0:
                dir = dir.replace(self.envPath + "src/", "")
            if directoryName.__len__() == 0:
                directoryName.append("app")
            # Creating directories in assets
            relativeDir = dir
            dir = self.envPath + "assets/" + dir
            valid = os.path.isdir(dir)
            if not valid:
                os.mkdir(dir)
            # Copy html, css files
            for f in file["files"]:
                directory = file["dir"]
                filePath = directory + "/" + f
                if f.find("component.ts") != -1 and f.find("component.spec.ts") == -1:
                    self.referenceTsFile(filePath, directory + "/", relativeDir)
                if f.find(".html") != -1:
                    self.referenceHtmlFile(filePath, f)
                if f.find(".html") != -1 or f.find(".css") != -1:
                    consoleManager(1, dir + "/" + f)
                    fileO = open(filePath, "r")
                    text = fileO.read()
                    fileO.close()
                    fileO = open(dir + "/" + f, "w")
                    fileO.write(text)
                    fileO.close()

    def referenceTsFile(self, path, dir, relativeDir):
        fileO = open(path, "r")
        text = fileO.read()
        fileO.close()
        ftpos = text.find("@Component")
        textRebuild = ""
        stclose = 0
        while ftpos != -1:
            ftpos = ftpos + 12
            stclose = ftpos
            ptoclose = 1
            while ptoclose > 0:
                if text[stclose] == "{":
                    ptoclose += 1
                if text[stclose] == "}":
                    ptoclose -= 1
                stclose += 1
            declaration = text[ftpos:stclose]
            templateUrl = re.search("(templateUrl[] *:[] * ').*'", declaration).group()
            templateUrlRem = re.search("(templateUrl[ ]*:[ './]*)", templateUrl).group()
            templateUrl = templateUrl.replace(templateUrlRem, "")
            templateUrl = templateUrl.replace("'", "")
            if templateUrl.find("o/") == -1:
                buildDir = "/o/" + self.appName + "/" + relativeDir + "/" + templateUrl
            else:
                buildDir = "/" + templateUrl
            buildDir = "templateUrl: '" + buildDir + "'"
            stPos = re.search("(templateUrl[] *:[] * ').*'", declaration).start()
            endPos = re.search("(templateUrl[] *:[] * ').*'", declaration).end()
            declarationBuild = text[ftpos - 12:stPos + ftpos] + buildDir + text[ftpos + endPos: stclose + 1]
            textRebuild += text[:ftpos - 12] + declarationBuild
            ftpos = text.find("@Component", ftpos)
            if ftpos != -1:
                declarationBuild += text[stclose + 1:ftpos - 12]
        textRebuild += text[stclose + 1:]
        fileO = open(path, "w")
        fileO.write(textRebuild)
        fileO.close()

    def referenceHtmlFile(self, path, filename):
        filename = filename.replace("html", "css")
        fileO = open(path, "r")
        text = fileO.read()
        fileO.close()
        textRebuild = ""
        if text.find(filename) == -1:
            textRebuild = "<head>" + "<link rel=\"stylesheet\" href=\"" + filename + "\"></head>" + text
        else:
            textRebuild = text
        fileO = open(path, "w")
        fileO.write(textRebuild)
        fileO.close()

    def copytree(self, src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    @staticmethod
    def getNgModuleStartCloseDeclaration(text):
        startPos = text.find("@NgModule")
        startPos += 9
        i = startPos
        numToClose = 0
        prevState = 0
        resText = ""
        numToClose2 = 0
        while numToClose >= 0:
            prevState = numToClose
            if text[i] == "}":
                numToClose2 -= 1
            if text[i] == ")":
                numToClose -= 1
            if numToClose >= 1 and numToClose2 >= 1:
                resText += text[i]
            if text[i] == "{":
                numToClose2 += 1
            if text[i] == "(":
                numToClose += 1
            i += 1
            if prevState == 1 and numToClose == 0:
                numToClose = -1
        return resText

    def rebuildNgModuleDeclaration(self, text, declaration):
        startPos = text.find("@NgModule")
        startPos += 9
        i = startPos
        rebuildedString = text[:startPos]
        declaration = declaration.replace("\"", "")
        rebuildedString += declaration
        numToClose = 0
        while numToClose >= 0:
            prevState = numToClose
            if text[i] == "(":
                numToClose += 1
            if text[i] == ")":
                numToClose -= 1
            i += 1
            if prevState == 1 and numToClose == 0:
                numToClose = -1
        restPart = text[i + 1:]
        rebuildedString += restPart
        return rebuildedString


def checkDir(path):
    valid = os.path.isdir(path)
    if not valid:
        exitError(1, path)
    consoleManager(1, path)


def dirExist(path):
    return os.path.isdir(path)


def checkFile(path):
    valid = os.path.isfile(path)
    if not valid:
        exitError(1, path)
    consoleManager(1, path)


def exitError(code, msg):
    if code == 1:
        consoleManager(3, msg + " doesn't exist")
        input("Press Enter to continue...")
        exit(1)
    if code == 2:
        consoleManager(3, msg)
        input("Press Enter to continue...")
        exit(2)


def consoleManager(code, log, endl=0):
    if endl == 1:
        print()
    if code == 1:
        print("INFO " + log)
    if code == 2:
        print("WARN " + log)
    if code == 3:
        print("ERROR " + log)


moduleCheck = ModuleCheckProject()
