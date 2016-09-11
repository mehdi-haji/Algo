class Library:
    name = None
    dependencies = []
    buildTime = 0
    totalBuildTime = 0
    isTotalBuildTimeComputed = False

    def __init__(self, name, buildTime):
        self.name = name
        self.buildTime = buildTime
        self.dependencies = []
        self.totalBuildTime = 0
        self.isTotalBuildTimeComputed = False

    def getTotalBuildTime(self):
        if self.isTotalBuildTimeComputed:
            return self.totalBuildTime

        if self.dependencies is None or len(self.dependencies) == 0:
            self.totalBuildTime = self.buildTime
            self.isTotalBuildTimeComputed = True
            return self.buildTime

        maxBuildTimeDependency = 0
        for dependency in self.dependencies:
            buildTimeDependency = dependency.getTotalBuildTime()
            maxBuildTimeDependency = max(maxBuildTimeDependency, buildTimeDependency)

        self.totalBuildTime = maxBuildTimeDependency + self.buildTime
        self.isTotalBuildTimeComputed = True
        return self.totalBuildTime

def test1():
#
#          libF ----------<------------
#                                     |
#                                     |
#          libE ---<--- libC ---<--- libB ---<--- libA
#                        |                          |
#                        |                          |
#                        ------------<---------------
#
#
    libA = Library("libA", 10)
    libB = Library("libB", 10)
    libC = Library("libC", 10)
    libD = Library("libD", 10)
    libE = Library("libE", 10)
    libF = Library("libF", 10)

    libA.dependencies.append(libB)
    libA.dependencies.append(libC)
    libB.dependencies.append(libC)
    libB.dependencies.append(libF)
    libC.dependencies.append(libE)

    totalBuildTime = libA.getTotalBuildTime()
    print("total build time = " + str(totalBuildTime))

test1()
