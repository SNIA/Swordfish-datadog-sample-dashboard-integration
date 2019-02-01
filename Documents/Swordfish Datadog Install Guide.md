
<a name="section"></a>

![https://www.snia.org/sites/default/files/SMI/member-logos/SNIA_SwordfishLogo%20Tag.jpg](media/31f6d669644d7fa491ff3b007c3e5b34.jpg)

**SNIA SwordfishTM Datadog Sample Integration Installation Guide**

The purpose of this Installation Guide is to illustrate the installation process
which will enable Datadog integration to a Swordfish service, and display of
system capacity information and available capacity thresholds. Developer and
user guides are also available.

- [Disclaimer](#disclaimer)
    + [SNIA Swordfish Sample Integration Dashboard for Datadog](#snia-swordfish-sample-integration-dashboard-for-datadog)
  * [Brief Working Functionality](#brief-working-functionality-)
    + [Steps to install and run Datadog Agent](#steps-to-install-and-run-datadog-agent-)
    + [To Configure Sample Dashboard](#to-configure-sample-dashboard-)


Disclaimer
==========

The information contained in this publication is subject to change without
notice. The SNIA makes no warranty of any kind with regard to this
specification, including, but not limited to, the implied warranties of
merchantability and fitness for a particular purpose. The SNIA shall not be
liable for errors contained herein or for incidental or consequential damages in
connection with the furnishing, performance, or use.

Suggestions for revisions should be directed to http://www.snia.org/feedback/.

Copyright © 2016-2019 Storage Networking Industry Association.

[Top](#section)

**Introduction**:

SNIA Swordfish™ Specification

The SNIA Swordfish™ specification helps to provide a unified approach for the
management of storage and servers in hyperscale and cloud infrastructure
environments, making it easier for IT administrators to integrate scalable
solutions into their data centers. SNIA Swordfish is an extension of the DMTF
Redfish specification, so the same easy-to-use RESTful interface is used, along
with JavaScript Object Notation (JSON) and Open Data Protocol (OData), to
seamlessly manage storage equipment and storage services in addition to servers.

SNIA Swordfish is designed to integrate with the technologies used in cloud data
center environments and can be used to accomplish a broad range of storage
management tasks from the simple to the advanced.

SNIA Swordfish has been designed around management use cases that focus on what
IT administrators need to do with storage equipment and storage services in a
data center. As a result, the API provides functionality that simplifies the way
storage can be allocated, monitored, and managed.

SNIA Swordfish™ Datadog Sample Integration

The Swordfish Datadog sample dashboard integration provides a dashboard for the
Datadog monitoring service that can connect to a Swordfish service (including
the Swordfish emulator), and provides an integration to the Datadog UI. It
provides connectivity to a Swordfish service and displays system capacity
information trending over time, configured capacity thresholds, and alert
information based on crossing those thresholds.

Datadog ([www.datadoghq.com](http://www.datadoghq.com)) is a monitoring service
for cloud-scale applications, providing monitoring of servers, databases, tools,
and services, through a SaaS based data analytics platform. Datadog enables
developers and operations teams see infrastructure, including cloud, servers,
apps, services, metrics, and more, all in one place. This includes real-time
interactive dashboards that can be customized to specific needs, full-text
search capabilities for metrics and events, sharing and discussion tools so
teams can collaborate using the insights they surface, targeted alerts for
critical issues, and API access to accommodate unique infrastructures.

[Top](#section)

### SNIA Swordfish Sample Integration Dashboard for Datadog

There are two functional components that, together, make up the SNIA SwordfishTM
Datadog Sample Integration Dashboard functionality: the Datadog agent that
collects information from the Swordfish APIs on the storage systems, and the
Swordfish dashboard capability in the Datadog monitoring service.

Datadog Agent:

>   The Datadog Agent is a piece of software that runs on any host (or set of
>   hosts if high availability configuration is required). Its job is to
>   faithfully collect events and metrics and bring them to Datadog in order to
>   present and manipulate the monitoring and performance data within the
>   dashboard. The Datadog Agent is open source; view the source code on GitHub
>   [(github.com/DataDog](https://github.com/DataDog)).

Swordfish Dashboard sample functionality:

-   Swordfish Dashboard views: Capacity data and threshold values for different
    collections like Volumes, Storage pools and filesystems.

-   Data Collection: Using different custom metrics, data-dog will collect all
    the required data and visualize it in to a Graph or Gauge.

[Top](#section)

Brief Working Functionality
----------------------------

-   Install the Swordfish Emulator in local or host machines or vm.

-   Install Datadog agent in each of the environment locations including vm,
    server, instances, container and running hosts.

-   Configure Datadog to collect data from the Swordfish emulator where it’s
    running.

-   Submit custom application metrics by writing code (not clear on this step?)

-   Open https://www.datadoghq.com in browser or user agent.

-   Register and login to <https://www.datadoghq.com>.

-   Create Datadog dashboards to show the required data in graphs. Instrument
    your own gauges, counters, timers and histograms.

[Top](#section)

### Steps to install and run Datadog Agent

1.  Before installing Datadog, the Swordfish Emulator should be running in local
    machine or Server machines to be the source of raw data to the Datadog
    dashboard.

>   Refer to the Swordfish Emulator Installation documentation to find steps to
>   install swordfish emulator in windows or linux systems. Additional steps to
>   configure local machines are described in developers documentation (Python
>   and SNIA emulator need to be installed.)  
>   **Where?**

1.  After installing the Swordfish Emulator on your network, you can now install
    Datadog.

2.  Login to the Datadog web site ( <https://app.datadoghq.com/> )  
    **…a few more instructions/guidance needed here to get to Step 4**

3.  Create API keys and Application keys
    (<https://app.datadoghq.com/account/settings#api/>) which we have to use in
    our local services. Note: A Datadog account required.

![](media/1ba1edb0e25e049dfc8b297fc0a3ad7b.png)

>   Need more instructions on creating API and Applications keys.

1.  Install Datadog to a Local machine.

>   Recommend: Ubuntu 16.04 (Swordfish tested configuration)

>   Also supported: Windows 7, 8 and 10

>   Should generate install steps for common OS’s, not just Ubuntu…

1.  *Installation Steps: (Provided information for Ubuntu Linux configuration)*

    Run the below commands to install Datadog in local machine.

    -   sudo apt-get update

    -   sudo apt-get install apt-transport-https

>   Set Datadog deb repo on local and import Datadog api key.

-   sudo sh -c "echo 'deb https://apt.datadoghq.com/ stable 6' \>
    /etc/apt/sources.list.d/datadog.list"

-   sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
    382E94DE

>   Use local apt repo and install the agent

-   sudo apt-get update

-   sudo apt-get install datadog-agent

>   Place our API key and copy it to config

-   sudo sh -c "sed 's/api_key:.\*/api_key: a7bf617d0e83ce090b870bc3853019c3/'
    /etc/datadog-agent/datadog.yaml.example \> /etc/datadog-agent/datadog.yaml"

>   Start Agent

-   sudo systemctl restart datadog-agent.service

1.  *Start Datadog :-*

    Start Agent as a service

-   sudo /etc/init.d/datadog-agent start

>   Restart agent running as a service

-   sudo /etc/init.d/datadog-agent restart

>   Status page of running agent

>   sudo /etc/init.d/datadog-agent info

[Top](#section)

### To Configure Sample Dashboard:

-   A new dashboard can be created from left menu of Datadog page.

    -   Click on Dashboard -\> New Dashboard

-   After creating dashboard, graphs can be selected by dragging widgets onto
    the board to visualize the data.

![](media/cba512a32433d136a49ea80b467ac9e8.png)

The below is the graph editor window where we can edit the visualization, choose
metrics and events, adds filters and add functionalities if required.

![](media/e5ae833574488566e3281e77e2497afe.png)

[Top](#section)

Additional information on the SNIA Swordfish specification and use is available
at https://www.snia.org/swordfish and <https://github.com/SNIA>.
