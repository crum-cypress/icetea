echo "Start to build"


properties ([
    buildDiscarder(
        logRotator(
            artifactDaysToKeepStr: '',
            artifactNumToKeepStr: '',
            daysToKeepStr: '30',
            numToKeepStr: '100'
        )
    )
])


timestamps {
    timeout(time: 30, unit: "MINUTES") {
        parallel(
            "stream linux": {
                node('linux') {
                    deleteDir()
                    dir("mbed-clitest"){
                        stage("Checkout linux source") {
                            echo "hello world!"
                            checkout scm
                        }

                        def pipeline = load "pipeline.groovy"

                        pipeline.baseBuild('linux')
                    }

                    // clean up
                    step([$class: 'WsCleanup'])
                }
            },
            "stream windows": {
                node('windows') {
                    deleteDir()
                    dir("mbed-clitest"){
                        stage("Checkout windows source") {
                            echo "hello world!"
                            checkout scm
                        }

                        def pipeline = load "pipeline.groovy"

                        pipeline.baseBuild('windows')
                    }

                    // clean up
                    step([$class: 'WsCleanup'])
                }
            },
            "stream example cliapp": {
                node('arm-none-eabi-gcc') {
                    deleteDir()
                    try {
                        dir("mbed-clitest"){
                            def pipeline = null
                            stage ("deploy") {
                                checkout scm
                                pipeline = load "pipeline.groovy"
                            }

                            if (pipeline) {
                                pipeline.buildExampleApp()
                            }
                        }
                    } catch (err) {
                        throw err
                    } finally {
                        // clean up
                        step([$class: 'WsCleanup'])
                    }
                }
            }
        )
    }
}