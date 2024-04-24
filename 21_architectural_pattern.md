# MONOLITHIC APPS
monolithic architecture adalah pattern dimana aplikasi handle requests, execute business logic, interaction dengan db
dan create html untuk front end.
simplenya 1 aplikasi melakukan segalanya, its inner components are highly coupled and deployed as one unit

# MICROSERVICES APPS
microservice architecture adalah patter dimana highly cohesive, loosely coupled services terpisah developmentnya
maintained, dan deployed. setipa component handle individual function, dan ketika terkombinasi,
applikasi handles semua business function

# SOA (SERVICE ORIENTED ARCHITECTURE)
mendefinisikan cara untuk membuat software component reusable via service Interfaces.
These interfaces utilize common communication standards in such a way that they can be rapidly incorporated into 
new applications without having to perform deep integration each time.

# SERVERLESS
serverless architecture adalah architecture dimana developer build dan runs aplikasi tanpa
provisioning atau managing servers. dengan cloud computing / serverless.
server ada tapi di managed oleh cloud provider.
resources digunakan untuk apa yang mereka butuhkan, on demand and sering using auto scaling.

# TWELVE FACTOR APPS
Twelve-Factor Apps

The Twelve-Factor App is a methodology for building scalable and maintainable software-as-a-service (SaaS) applications. It is based on a set of best practices that were identified by the authors of the methodology as being essential for building modern, cloud-native applications.

The Twelve-Factor App methodology consists of the following principles:

    Codebase: There should be a single codebase for the application, with multiple deployments.
    Dependencies: The application should explicitly declare and isolate its dependencies.
    Config: The application should store configuration in the environment.
    Backing services: The application should treat backing services as attached resources.
    Build, release, run: The application should be built, released, and run as an isolated unit.
    Processes: The application should be executed as one or more stateless processes.
    Port binding: The application should expose its services through port binding.
    Concurrency: The application should scale out by adding more processes, not by adding threads.
    Disposability: The application should be designed to start and stop quickly.
    Dev/prod parity: The development, staging, and production environments should be as similar as possible.
    Logs: The application should treat logs as event streams.
    Admin processes: The application should run admin/maintenance tasks as one-off processes.





