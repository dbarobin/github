API
For other uses, see API (disambiguation).
"Api.php" redirects here. For the Wikipedia API, see Special:ApiHelp.
An application programming interface (API) is a way for two or more computer programs or components to communicate with each other. It is a type of software interface, offering a service to other pieces of software.[1] A document or standard that describes how to build or use such a connection or interface is called an API specification. A computer system that meets this standard is said to implement or expose an API. The term API may refer either to the specification or to the implementation. Whereas a system's user interface dictates how its end-users interact with the system in question, its API dictates how to write code that takes advantage of that system's capabilities.


Screenshot of web API documentation written by NASA demonstrating the use of APOD.
In contrast to a user interface, which connects a computer to a person, an application programming interface connects computers or pieces of software to each other. It is not intended to be used directly by a person (the end user) other than a computer programmer who is incorporating it into the software. An API is often made up of different parts which act as tools or services that are available to the programmer. A program or a programmer that uses one of these parts is said to call that portion of the API. The calls that make up the API are also known as subroutines, methods, requests, or endpoints. An API specification defines these calls, meaning that it explains how to use or implement them.

One purpose of APIs is to hide the internal details of how a system works, exposing only those parts that a programmer will find useful, and keeping them consistent even if the internal details change later. An API may be custom-built for a particular pair of systems, or it may be a shared standard allowing interoperability among many systems.

There are APIs for programming languages, software libraries, computer operating systems, and computer hardware. APIs originated in the 1940s, though the term did not emerge until the 1960s and 1970s. Contemporary usage of the term API often refers to web APIs,[2] which allow communication between computers that are joined by the internet. Recent developments in APIs have led to the rise in popularity of microservices, which are loosely coupled services accessed through public APIs.[3]

Purpose

In building applications, an API simplifies programming by abstracting the underlying implementation and only exposing objects or actions the developer needs. While a graphical interface for an email client might provide a user with a button that performs all the steps for fetching and highlighting new emails, an API for file input/output might give the developer a function that copies a file from one location to another without requiring that the developer understand the file system operations occurring behind the scenes.[4]

History of the term


A diagram from 1978 proposing the expansion of the idea of the API to become a general programming interface, beyond application programs alone[5]
The term API initially described an interface only for end-user-facing programs, known as application programs. This origin is still reflected in the name "application programming interface." Today, the term is broader, including also utility software and even hardware interfaces.[6]

1940s and 50s

The idea of the API is much older than the term itself. British computer scientists Maurice Wilkes and David Wheeler worked on a modular software library in the 1940s for EDSAC, an early computer. The subroutines in this library were stored on punched paper tape organized in a filing cabinet. This cabinet also contained what Wilkes and Wheeler called a "library catalog" of notes about each subroutine and how to incorporate it into a program. Today, such a catalog would be called an API (or an API specification or API documentation) because it instructs a programmer on how to use (or "call") each subroutine that the programmer needs.[6]

Wilkes and Wheeler's 1951 book The Preparation of Programs for an Electronic Digital Computer contains the first published API specification. Joshua Bloch considers that Wilkes and Wheeler "latently invented" the API because it is more of a concept that is discovered than invented.[6]


Although the people who coined the term API were implementing software on a Univac 1108, the goal of their API was to make hardware independent programs possible.[7]
1960s and 70s

The term "application program interface" (without an ‑ing suffix) is first recorded in a paper called Data structures and techniques for remote computer graphics presented at an AFIPS conference in 1968.[8][6] The authors of this paper use the term to describe the interaction of an application—a graphics program in this case—with the rest of the computer system. A consistent application interface (consisting of Fortran subroutine calls) was intended to free the programmer from dealing with idiosyncrasies of the graphics display device, and to provide hardware independence if the computer or the display were replaced.[7]

The term was introduced to the field of databases by C. J. Date[9] in a 1974 paper called The Relational and Network Approaches: Comparison of the Application Programming Interface.[10] An API became a part of the ANSI/SPARC framework for database management systems. This framework treated the application programming interface separately from other interfaces, such as the query interface. Database professionals in the 1970s observed these different interfaces could be combined; a sufficiently rich application interface could support the other interfaces as well.[5]

This observation led to APIs that supported all types of programming, not just application programming.

1990s

By 1990, the API was defined simply as "a set of services available to a programmer for performing certain tasks" by technologist Carl Malamud.[11]

The idea of the API was expanded again with the dawn of remote procedure calls and web APIs. As computer networks became common in the 1970s and 1980s, programmers wanted to call libraries located not only on their local computers but on computers located elsewhere. These remote procedure calls were well supported by the Java language in particular. In the 1990s, with the spread of the internet, standards like CORBA, COM, and DCOM competed to become the most common way to expose API services.[12]

2000s

Roy Fielding's dissertation Architectural Styles and the Design of Network-based Software Architectures at UC Irvine in 2000 outlined Representational state transfer (REST) and described the idea of a "network-based Application Programming Interface" that Fielding contrasted with traditional "library-based" APIs.[13] XML and JSON web APIs saw widespread commercial adoption beginning in 2000 and continuing as of 2022. The web API is now the most common meaning of the term API.[2]

The Semantic Web proposed by Tim Berners-Lee in 2001 included "semantic APIs" that recasts the API as an open, distributed data interface rather than a software behavior interface.[14] Proprietary interfaces and agents became more widespread than open ones, but the idea of the API as a data interface took hold. Because web APIs are widely used to exchange data of all kinds online, API has become a broad term describing much of the communication on the internet.[12] When used in this way, the term API has overlap in meaning with the term communication protocol.

Usage

Libraries and frameworks

The interface to a software library is one type of API. The API describes and prescribes the "expected behavior" (a specification) while the library is an "actual implementation" of this set of rules.

A single API can have multiple implementations (or none, being abstract) in the form of different libraries that share the same programming interface.

The separation of the API from its implementation can allow programs written in one language to use a library written in another. For example, because Scala and Java compile to compatible bytecode, Scala developers can take advantage of any Java API.[15]

API use can vary depending on the type of programming language involved. An API for a procedural language such as Lua could consist primarily of basic routines to execute code, manipulate data or handle errors while an API for an object-oriented language, such as Java, would provide a specification of classes and its class methods.[16][17] Hyrum's law[18] states that "With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody." Meanwhile, several studies show that most applications that use an API tend to use a small part of the API.[19]

Language bindings are also APIs. By mapping the features and capabilities of one language to an interface implemented in another language, a language binding allows a library or service written in one language to be used when developing in another language.[citation needed]

Tools such as SWIG and F2PY, a Fortran-to-Python interface generator, facilitate the creation of such interfaces.[20]

An API can also be related to a software framework: a framework can be based on several libraries implementing several APIs, but unlike the normal use of an API, the access to the behavior built into the framework is mediated by extending its content with new classes plugged into the framework itself.

Moreover, the overall program flow of control can be out of the control of the caller and in the framework's hands by inversion of control or a similar mechanism.[21][22]

Operating systems

An API can specify the interface between an application and the operating system.[23] POSIX, for example, provides a set of common API specifications that aim to enable an application written for a POSIX conformant operating system to be compiled for another POSIX conformant operating system.

Linux and Berkeley Software Distribution are examples of operating systems that implement the POSIX APIs.[24]

Microsoft has shown a strong commitment to a backward-compatible API, particularly within its Windows API (Win32) library, so older applications may run on newer versions of Windows using an executable-specific setting called "Compatibility Mode".[25]

An API differs from an application binary interface (ABI) in that an API is source code based while an ABI is binary based. For instance, POSIX provides APIs while the Linux Standard Base provides an ABI.[26][27]

Remote APIs

Remote APIs allow developers to manipulate remote resources through protocols, specific standards for communication that allow different technologies to work together, regardless of language or platform. For example, the Java Database Connectivity API allows developers to query many different types of databases with the same set of functions, while the Java remote method invocation API uses the Java Remote Method Protocol to allow invocation of functions that operate remotely but appear local to the developer.[28][29]

Therefore, remote APIs are useful in maintaining the object abstraction in object-oriented programming; a method call, executed locally on a proxy object, invokes the corresponding method on the remote object, using the remoting protocol, and acquires the result to be used locally as a return value.

A modification of the proxy object will also result in a corresponding modification of the remote object.[30]

Web APIs

Main article: Web API
Web APIs are a service accessed from client devices (mobile phones, laptops, etc.) to a web server using the Hypertext Transfer Protocol (HTTP). Client devices send a request in the form of an HTTP request, and are met with a response message usually in JavaScript Object Notation (JSON) or Extensible Markup Language (XML) format. Developers typically use Web APIs to query a server for a specific set of data from that server.

An example might be a shipping company API that can be added to an eCommerce-focused website to facilitate ordering shipping services and automatically include current shipping rates, without the site developer having to enter the shipper's rate table into a web database. While "web API" historically has been virtually synonymous with web service, the recent trend (so-called Web 2.0) has been moving away from Simple Object Access Protocol (SOAP) based web services and service-oriented architecture (SOA) towards more direct representational state transfer (REST) style web resources and resource-oriented architecture (ROA).[31] Part of this trend is related to the Semantic Web movement toward Resource Description Framework (RDF), a concept to promote web-based ontology engineering technologies. Web APIs allow the combination of multiple APIs into new applications known as mashups.[32]

In the social media space, web APIs have allowed web communities to facilitate sharing content and data between communities and applications. In this way, content that is created in one place dynamically can be posted and updated to multiple locations on the web.[33] For example, Twitter's REST API allows developers to access core Twitter data and the Search API provides methods for developers to interact with Twitter Search and trends data.[34]

Design

The design of an API has a significant impact on its usage.[4] First of all, the design of programming interfaces represents an important part of software architecture, the organization of a complex piece of software.[35] The principle of information hiding describes the role of programming interfaces as enabling modular programming by hiding the implementation details of the modules so that users of modules need not understand the complexities inside the modules.[36] Aside from the previous underlying principle, other metrics for measuring the usability of an API may include properties such as functional efficiency, overall correctness, and learnability for novices.[37] One straightforward and commonly adopted way of designing APIs is to follow Nielsen's heuristic evaluation guidelines. The Factory method pattern is also typical in designing APIs due to their reusable nature.[38] Thus, the design of an API attempts to provide only the tools a user would expect.[4]

Synchronous versus asynchronous

An application programming interface can be synchronous or asynchronous. A synchronous API call is a design pattern where the call site is blocked while waiting for the called code to finish.[39] With an asynchronous API call, however, the call site is not blocked while waiting for the called code to finish, and instead the calling thread is notified when the reply arrives.

Security

API security is very critical when developing a public facing API. Common threats include SQL injection, Denial-of-service attack (DoS), broken authentication, and exposing sensitive data.[40] Without ensuring proper security practices, bad actors can get access to information they should not have or even gain privileges to make changes to your server. Some common security practices include proper connection security using HTTPS, content security to mitigate data injection attacks, and requiring an API key to use your service.[41] Many public facing API services require you to use an assigned API key, and will refuse to serve data without sending the key with your request.[42]

Release policies

APIs are one of the more common ways technology companies integrate. Those that provide and use APIs are considered as being members of a business ecosystem.[43]

The main policies for releasing an API are:[44]

Private: The API is for internal company use only.
Partner: Only specific business partners can use the API. For example, vehicle for hire companies such as Uber and Lyft allow approved third-party developers to directly order rides from within their apps. This allows the companies to exercise quality control by curating which apps have access to the API and provides them with an additional revenue stream.[45]
Public: The API is available for use by the public. For example, Microsoft makes the Windows API public, and Apple releases its API Cocoa so that software can be written for their platforms. Not all public APIs are generally accessible by everybody. For example, Internet service providers like Cloudflare or Voxility, use RESTful APIs to allow customers and resellers access to their infrastructure information, DDoS stats, network performance, or dashboard controls.[46] Access to such APIs is granted either by "API tokens", or customer status validations.[47]
Public API implications

An important factor when an API becomes public is its "interface stability". Changes to the API—for example adding new parameters to a function call—could break compatibility with the clients that depend on that API.[48]

When parts of a publicly presented API are subject to change and thus not stable, such parts of a particular API should be documented explicitly as "unstable". For example, in the Google Guava library, the parts that are considered unstable, and that might change soon, are marked with the Java annotation @Beta.[49]

A public API can sometimes declare parts of itself as deprecated or rescinded. This usually means that part of the API should be considered a candidate for being removed, or modified in a backward incompatible way. Therefore, these changes allow developers to transition away from parts of the API that will be removed or not supported in the future.[50]

On February 19, 2020, Akamai published their annual "State of the Internet" report, showcasing the growing trend of cybercriminals targeting public API platforms at financial services worldwide. From December 2017 through November 2019, Akamai witnessed 85.42 billion credential violation attacks. About 20%, or 16.55 billion, were against hostnames defined as API endpoints. Of these, 473.5 million have targeted financial services sector organizations.[51]

Documentation

API documentation describes the services an API offers and how to use those services, aiming to cover everything a client would need to know for practical purposes.

Documentation is crucial for the development and maintenance of applications using the API.[52] API documentation is traditionally found in documentation files but can also be found in social media such as blogs, forums, and Q&A websites.[53]

Traditional documentation files are often presented via a documentation system, such as Javadoc or Pydoc, that has a consistent appearance and structure. However, the types of content included in the documentation differ from API to API.[54]

In the interest of clarity, API documentation may include a description of classes and methods in the API as well as "typical usage scenarios, code snippets, design rationales, performance discussions, and contracts", but implementation details of the API services themselves are usually omitted.

Reference documentation for a REST API can be generated automatically from an OpenAPI document, which is a machine-readable text file that uses a prescribed format and syntax defined in the OpenAPI Specification. The OpenAPI document defines basic information such as the API's name and description, as well as describing operations the API provides access to.[55]

API documentation can be enriched with metadata information like Java annotations. This metadata can be used by the compiler, tools, and by the run-time environment to implement custom behaviors or custom handling.[56]

Dispute over copyright protection for APIs

Main article: Oracle America, Inc. v. Google, Inc.
In 2010, Oracle Corporation sued Google for having distributed a new implementation of Java embedded in the Android operating system.[57] Google had not acquired any permission to reproduce the Java API, although permission had been given to the similar OpenJDK project. Google had approached Oracle to negotiate a license for their API, but were turned down due to trust issues. Despite the disagreement, Google chose to use Oracle's code anyway. Judge William Alsup ruled in the Oracle v. Google case that APIs cannot be copyrighted in the U.S and that a victory for Oracle would have widely expanded copyright protection to a "functional set of symbols" and allowed the copyrighting of simple software commands:

To accept Oracle's claim would be to allow anyone to copyright one version of code to carry out a system of commands and thereby bar all others from writing its different versions to carry out all or part of the same commands.[58][59]

Alsup's ruling was overturned in 2014 on appeal to the Court of Appeals for the Federal Circuit, though the question of whether such use of APIs constitutes fair use was left unresolved.[60][61]

In 2016, following a two-week trial, a jury determined that Google's reimplementation of the Java API constituted fair use, but Oracle vowed to appeal the decision.[62] Oracle won on its appeal, with the Court of Appeals for the Federal Circuit ruling that Google's use of the APIs did not qualify for fair use.[63] In 2019, Google appealed to the Supreme Court of the United States over both the copyrightability and fair use rulings, and the Supreme Court granted review.[64] Due to the COVID-19 pandemic, the oral hearings in the case were delayed until October 2020.[65]

The case was decided by the Supreme Court in Google's favor with a ruling of 6–2. Justice Stephen Breyer delivered the opinion of the court and at one point mentioned that "The declaring code is, if copyrightable at all, further than are most computer programs from the core of copyright." This means the code used in APIs are more similar to dictionaries than novels in terms of copyright protection.[66]

Examples

Main category: Application programming interfaces
ASPI for SCSI device interfacing
Cocoa and Carbon for the Macintosh
DirectX for Microsoft Windows
Ark Engine for HarmonyOS
EHLLAPI
Java APIs
ODBC for Microsoft Windows
OpenAL cross-platform sound API
OpenCL cross-platform API for general-purpose computing for CPUs & GPUs
OpenGL cross-platform graphics API
OpenMP API that supports multi-platform shared memory multiprocessing programming in C, C++, and Fortran on many architectures, including Unix and Microsoft Windows platforms.
Server application programming interface (SAPI)
Simple DirectMedia Layer (SDL)
See also

API testing
API writer
Augmented web
Calling convention
Common Object Request Broker Architecture (CORBA)
Comparison of application virtual machines
Document Object Model (DOM)
Double-chance function
Foreign function interface
Front and back ends
Interface (computing)
Interface control document
List of 3D graphics APIs
Microservices
Name mangling
Open API
Open Service Interface Definitions
Parsing
Plugin
RAML (software)
Software development kit (SDK)
Structured Financial Messaging System
Web API
Web content vendor
XPCOM
References

Reddy, Martin (2011). API Design for C++. Elsevier Science. p. 1. ISBN 9780123850041.normal
^ a b Lane, Kin (October 10, 2019). "Intro to APIs: History of APIs". Postman. Retrieved September 18, 2020. When you hear the acronym "API" or its expanded version "Application Programming Interface", it is almost always in reference to our modern approach, in that we use HTTP to provide access to machine readable data in a JSON or XML format, often simply referred to as "web APIs." APIs have been around almost as long as computing, but modern web APIs began taking shape in the early 2000s.normal
Wood, Laura (2021-08-25). "Global Cloud Microservices Market (2021 to 2026)". businesswire.com. Retrieved 2022-03-29.normal
^ a b c Clarke, Steven (2004). "Measuring API Usability". Dr. Dobb's. Retrieved 29 July 2016.normal
^ a b Database architectures – a feasibility workshop (Report). Washington, DC: U.S. Department of Commerce, National Bureau of Standards. April 1981. pp. 45–47. hdl:2027/mdp.39015077587742. LCCN 81600004. NBS special publication 500-76. Retrieved September 18, 2020.normal
^ a b c d Bloch, Joshua (August 8, 2018). A Brief, Opinionated History of the API (Speech). QCon. San Francisco: InfoQ. Retrieved September 18, 2020.normal
^ a b Cotton, Ira W.; Greatorex, Frank S. (December 1968). "Data structures and techniques for remote computer graphics". AFIPS '68: Proceedings of the December 9–11, 1968, Fall Joint Computer Conference. AFIPS 1968 Fall Joint Computer Conference. Vol. I. San Francisco, California: Association for Computing Machinery. pp. 533–544. doi:10.1145/1476589.1476661. ISBN 978-1450378994. OCLC 1175621908.normal
"application program interface". Oxford English Dictionary (Online ed.). Oxford University Press.normal (Subscription or participating institution membership required.)
^ Date, C. J. (2019). E. F. Codd and Relational Theory: A Detailed Review and Analysis of Codd's Major Database Writings. Lulu.com. p. 135. ISBN 978-1684705276.
^ Date, C. J.; Codd, E. F. (January 1975). "The relational and network approaches: Comparison of the application programming interfaces". In Randall Rustin (ed.). Proceedings of 1974 ACM-SIGMOD Workshop on Data Description, Access and Control. SIGMOD Workshop 1974. Vol. 2. Ann Arbor, Michigan: Association for Computing Machinery. pp. 83–113. doi:10.1145/800297.811532. ISBN 978-1450374187. OCLC 1175623233.
^ Carl, Malamud (1990). Analyzing Novell Networks. Van Nostrand Reinhold. p. 294. ISBN 978-0442003647.
^ a b Jin, Brenda; Sahni, Saurabh; Shevat, Amir (2018). Designing Web APIs. O'Reilly Media. ISBN 9781492026877.
^ Fielding, Roy (2000). Architectural Styles and the Design of Network-based Software Architectures (PhD). University of California, Irvine. Retrieved September 18, 2020.
^ Dotsika, Fefie (August 2010). "Semantic APIs: Scaling up towards the Semantic Web". International Journal of Information Management. 30 (4): 335–342. doi:10.1016/j.ijinfomgt.2009.12.003.
^ Odersky, Martin; Spoon, Lex; Venners, Bill (10 December 2008). "Combining Scala and Java". artima.com. Retrieved 29 July 2016.
^ de Figueiredo, Luiz Henrique; Ierusalimschy, Roberto; Filho, Waldemar Celes (1994). "The design and implementation of a language for extending applications". TeCGraf Grupo de Tecnologia Em Computacao Grafica: 273–284. CiteSeerX 10.1.1.47.5194. S2CID 59833827. Retrieved 29 July 2016.
^ Sintes, Tony (13 July 2001). "Just what is the Java API anyway?". JavaWorld. Retrieved 2020-07-18.
^ Winters, Titus; Tom Manshreck; Hyrum Wright, eds. (2020). Software engineering at Google: lessons learned from programming over time. Sebastopol, CA: O'Reilly Media. ISBN 9781492082798. OCLC 1144086840.
^ Mastrangelo, Luis; Ponzanelli, Luca; Mocci, Andrea; Lanza, Michele; Hauswirth, Matthias; Nystrom, Nathaniel (2015-10-23). "Use at your own risk: the Java unsafe API in the wild". Proceedings of the 2015 ACM SIGPLAN International Conference on Object-Oriented Programming, Systems, Languages, and Applications. OOPSLA 2015. New York, NY, US: Association for Computing Machinery. pp. 695–710. doi:10.1145/2814270.2814313. ISBN 978-1-4503-3689-5.
^ "F2PY.org". F2PY.org. Retrieved 2011-12-18.
^ Fowler, Martin. "Inversion Of Control".
^ Fayad, Mohamed. "Object-Oriented Application Frameworks".
^ Lewine, Donald A. (1991). POSIX Programmer's Guide. O'Reilly & Associates, Inc. p. 1. ISBN 9780937175736. Retrieved 2 August 2016.
^ West, Joel; Dedrick, Jason (2001). "Open source standardization: the rise of Linux in the network era" (PDF). Knowledge, Technology & Policy. 14 (2): 88–112. doi:10.1007/PL00022278. S2CID 46082812. Retrieved 2 August 2016.
^ Microsoft (October 2001). "Support for Windows XP". Microsoft. p. 4. Archived from the original on 2009-09-26.
^ "LSB Introduction". Linux Foundation. 21 June 2012. Archived from the original on 2015-04-02. Retrieved 2015-03-27.
^ Stoughton, Nick (April 2005). "Update on Standards" (PDF). USENIX. Retrieved 2009-06-04.
^ Bierhoff, Kevin (23 April 2009). API Protocol Compliance in Object-Oriented Software (PDF) (PhD). Carnegie Mellon University. ISBN 978-1-109-31660-5. ProQuest 304864018. Retrieved 29 July 2016.
^ Wilson, M. Jeff (10 November 2000). "Get smart with proxies and RMI". JavaWorld. Retrieved 2020-07-18.
^ Henning, Michi; Vinoski, Steve (1999). Advanced CORBA Programming with C++. Addison-Wesley. ISBN 978-0201379273. Retrieved 16 June 2015.
^ Benslimane, Djamal; Schahram Dustdar; Amit Sheth (2008). "Services Mashups: The New Generation of Web Applications". IEEE Internet Computing, vol. 12, no. 5. Institute of Electrical and Electronics Engineers. pp. 13–15. Archived from the original on 2011-09-28. Retrieved 2019-10-01.[dead link]
^ Niccolai, James (2008-04-23), "So What Is an Enterprise Mashup, Anyway?", PC World, archived from the original on Oct 10, 2017
^ Parr, Ben (21 May 2009). "The Evolution of the Social Media API". Mashable. Archived from the original on Aug 11, 2016. Retrieved 26 July 2016.
^ "GET trends/place". Twitter Developer Platform. Retrieved 2020-04-30.
^ Garlan, David; Shaw, Mary (January 1994). "An Introduction to Software Architecture" (PDF). Advances in Software Engineering and Knowledge Engineering. 1. Retrieved 8 August 2016 – via CMU School of Computer Science.
^ Parnas, D.L. (1972). "On the Criteria To Be Used in Decomposing Systems into Modules". Communications of the ACM. 15 (12): 1053–1058. doi:10.1145/361598.361623. S2CID 53856438.
^ Myers, Brad A.; Stylos, Jeffrey (2016). "Improving API usability". Communications of the ACM. 59 (6): 62–69. doi:10.1145/2896587. S2CID 543853. Archived from the original on Dec 25, 2023.
^ Brian Ellis, Jeffrey Stylos, and Brad Myers. 2007. "The Factory Pattern in API Design: A Usability Evaluation". In Proceedings of the 29th international conference on Software Engineering (ICSE '07). IEEE Computer Society, USA, 302–312. doi:10.1109/ICSE.2007.85.
^ "Synchronous vs. Asynchronous Writes - Packaged Contact Center Enterprise" - Cisco DevNet.
^ Silva, Paulo (2019). "Global Cloud Microservices Market (2021 to 2026)". Retrieved 2022-03-29.
^ "Web Security". 2022-02-18. Retrieved 2022-03-29.
^ "API Keys – What Is an API Key? | APILayer Blog". 2022-03-01. Retrieved 2022-07-15.
^ de Ternay, Guerric (Oct 10, 2015). "Business Ecosystem: Creating an Economic Moat". BoostCompanies. Retrieved 2016-02-01.
^ Boyd, Mark (2014-02-21). "Private, Partner or Public: Which API Strategy Is Best for Business?". ProgrammableWeb. Retrieved 2 August 2016.
^ Weissbrot, Alison (7 July 2016). "Car Service APIs Are Everywhere, But What's In It For Partner Apps?". AdExchanger.
^ "Cloudflare API v4 Documentation". cloudflare. 25 February 2020. Retrieved 27 February 2020.
^ Liew, Zell (17 January 2018). "Car Service APIs Are Everywhere, But What's In It For Partner Apps". Smashing Magazine. Retrieved 27 February 2020.
^ Shi, Lin; Zhong, Hao; Xie, Tao; Li, Mingshu (2011). "An Empirical Study on Evolution of API Documentation". Fundamental Approaches to Software Engineering. International Conference on Fundamental Approaches to Software Engineering. Lecture Notes in Computer Science. Vol. 6603. pp. 416–431. doi:10.1007/978-3-642-19811-3_29. ISBN 978-3-642-19810-6. Retrieved 22 July 2016.
^ "guava-libraries – Guava: Google Core Libraries for Java 1.6+". Google Project Hosting. 2014-02-04. Archived from the original on Mar 26, 2014. Retrieved 2014-02-11.
^ Oracle. "How and When to Deprecate APIs". Java SE Documentation. Retrieved 2 August 2016.
^ Takanashi, Dean (19 February 2020). "Akamai: Cybercriminals are attacking APIs at financial services firms". Venture Beat. Retrieved 27 February 2020.
^ Dekel, Uri; Herbsleb, James D. (May 2009). "Improving API Documentation Usability with Knowledge Pushing". Institute for Software Research, School of Computer Science. CiteSeerX 10.1.1.446.4214.
^ Parnin, Chris; Treude, Cristoph (May 2011). "Measuring API documentation on the web". Web2SE '11: Proceedings of the 2nd International Workshop on Web 2.0 for Software Engineering. pp. 25–30. doi:10.1145/1984701.1984706. ISBN 9781450305952. S2CID 17751901.
^ Maalej, Waleed; Robillard, Martin P. (April 2012). "Patterns of Knowledge in API Reference Documentation" (PDF). IEEE Transactions on Software Engineering. Retrieved 22 July 2016.
^ "Structure of an OpenAPI Document". OpenAPI Documentation. Retrieved 2022-11-06.
^ "Annotations". Sun Microsystems. Archived from the original on 2011-09-25. Retrieved 2011-09-30..
^ "Oracle and the End of Programming As We Know It". DrDobbs. 2012-05-01. Retrieved 2012-05-09.
^ "APIs Can't be Copyrighted Says Judge in Oracle Case". TGDaily. 2012-06-01. Retrieved 2012-12-06.
^ "Oracle America, Inc. vs. Google Inc." (PDF). Wired. 2012-05-31. Retrieved 2013-09-22.
^ "Oracle Am., Inc. v. Google Inc., No. 13-1021, Fed. Cir. 2014". Archived from the original on 2014-10-10.
^ Rosenblatt, Seth (May 9, 2014). "Court sides with Oracle over Android in Java patent appeal". CNET. Retrieved 2014-05-10.
^ "Google beats Oracle – Android makes "fair use" of Java APIs". Ars Technica. 2016-05-26. Retrieved 2016-07-28.
^ Decker, Susan (March 27, 2018). "Oracle Wins Revival of Billion-Dollar Case Against Google". Bloomberg Businessweek. Retrieved March 27, 2018.
^ Lee, Timothy (January 25, 2019). "Google asks Supreme Court to overrule disastrous ruling on API copyrights". Ars Technica. Retrieved February 8, 2019.
^ vkimber (2020-09-28). "Google LLC v. Oracle America, Inc". LII / Legal Information Institute. Retrieved 2021-03-06.
^ "Supreme Court of the United States, No. 18–956, GOOGLE LLC, PETITIONER v. ORACLE AMERICA, INC" (PDF). April 5, 2021.
Further reading edit

Taina Bucher (16 November 2013). "Objects of Intense Feeling: The Case of the Twitter API". Computational Culture (3). ISSN 2047-2390. Argues that "APIs are far from neutral tools" and form a key part of contemporary programming, understood as a fundamental part of culture.
What is an API? – in the U.S. Supreme Court opinion, Google v. Oracle 2021, pp. 3–7 – "For each task, there is computer code; API (also known as Application Programming Interface) is the method for calling that 'computer code' (instruction – like a recipe – rather than cooking instruction, this is machine instruction) to be carry out"
Maury, Innovation and Change – Cory Ondrejka, February 28, 2014, " ...proposed a public API to let computers talk to each other". (Textise URL)
External links edit

Forrester : IT industry : API Case : Google v. Oracle – May 20, 2021 – content format: Audio with text – length 26:41
Geliştiriciler İçin API Listesi – Feb 23, 2024
Retrieved from "https://en.wikipedia.org/w/index.php?title=github=WIKIDATA"
