FROM openjdk:11-jdk as build

RUN useradd -ms /bin/bash spring
USER spring

WORKDIR /workspace/app

COPY gradlew .
COPY gradle gradle
COPY build.gradle .
COPY settings.gradle .
COPY src src

RUN ./gradlew clean build

RUN mkdir -p build/dependency && (cd build/dependency; java -Djarmode=layertools -jar ../libs/*.jar extract)

FROM openjdk:11-jre

RUN useradd -ms /bin/bash spring
USER spring

WORKDIR /app
COPY --from=build /workspace/app/build/dependency/dependencies/ ./
COPY --from=build /workspace/app/build/dependency/spring-boot-loader/ ./
COPY --from=build /workspace/app/build/dependency/snapshot-dependencies/ ./
COPY --from=build /workspace/app/build/dependency/application/ ./
ENTRYPOINT ["java", "org.springframework.boot.loader.JarLauncher"]