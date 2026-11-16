GITHUB = 'https://github.com/jillnguyen2311/'

PROJECTS = [{'id': 'sms360',
  'name': 'SMS360 / QLTH',
  'type': 'BachKhoaTech · School management',
  'category': 'systems',
  'role': 'Business Analyst',
  'when': 'May 2025 – July 2026',
  'status': 'Production product work',
  'tags': ['SRS', 'Release scoping', 'REST API', 'SQL'],
  'summary': 'How I specified a digital homeroom notebook and a school-wide grade-visibility rule for the web '
             'and mobile school management products.',
  'cover': ['Class + academic year', 'One notebook', 'Reporting checkpoints'],
  'sections': [('The school’s problem',
                'Teachers maintain a homeroom record with class details, plans and periodic reports. School '
                'leaders review the record and add comments. Schools also wanted to hide electronic gradebook '
                'averages while teachers were still entering component scores, because an incomplete average '
                'could be misread as a final result.'),
               ('My role in delivery',
                'I elicited requirements from school staff, reconciled competing requests with developers, and '
                'refined the Jira backlog against delivery capacity. I recorded release decisions in '
                'Confluence and used screen-level specifications and Figma to explain fields, permissions, '
                'form validation and outcomes to developers.'),
               ('Decision 1 · One record across terms',
                'A homeroom notebook belongs to a class and academic year. Opening it for the first time '
                'initializes the record with the relevant school-level template. A midyear or year-end '
                'checkpoint determines the content to show while pointing to the same record. The database '
                'specification covers this identity, the assigned teacher and reviewer, linked sections and '
                'change history.'),
               ('Decision 2 · A school-wide release first',
                'The first grade visibility release applies one configuration per school, academic year and '
                'semester. I documented role restrictions and the default when no active configuration exists. '
                'Class- and subject-level overrides were deferred. The API applies the resolved rule to the '
                'score response so web and mobile enforce the same behaviour.'),
               ('Validation and investigation',
                'I used SQL to verify teacher–subject records by school and subject. For missing conduct '
                'scores, the HTTP call succeeded, but the response data was empty and indicated that scores '
                'first had to be copied. That separated a missing source-data step from a transport failure. I '
                'also proposed that first-term grading proceed independently while digital report cards retain '
                'the annual gradebook dependency.')],
  'links': [('SMS360 product site', 'https://qlth.lms360.vn/')]},
 {'id': 'uni360',
  'name': 'UNI360',
  'type': 'Higher education · Systems design',
  'category': 'systems',
  'role': 'Business and systems analysis',
  'when': '2025–2026',
  'status': 'Design and UAT planning',
  'tags': ['ERD', 'BPMN', 'Business rules', 'UAT'],
  'summary': 'Requirements, data and process models for universities to manage academic structures and enroll '
             'students in the right course section.',
  'cover': ['Registration request', 'Eligibility checks', 'Enrollment'],
  'sections': [('The university’s problem',
                'Academic staff need to maintain programs, courses, year structures and sections. A student '
                'belongs to a cohort class, yet takes multiple course sections each term. Some sections are '
                'assigned to a cohort while electives may be selected by individuals.'),
               ('Separate cohort membership from enrollment',
                'I modelled a cohort class as an ongoing student grouping within a program. Course sections '
                'are separately scheduled offerings for a course and term. Enrollment is the relationship '
                'between a student and a section. This lets staff allocate seats or change a student’s section '
                'without changing their cohort.'),
               ('Registration and exceptions',
                'The specification covers both student self-registration and staff assignment. In '
                'self-registration, prerequisites, section capacity and schedule conflicts determine '
                'eligibility. The design also accounts for constraints such as preventing deletion of a '
                'section with active enrollments.'),
               ('Verification design',
                'I linked the rules to test cases for unmet prerequisites, full sections and overlapping '
                'times. The BPMN below follows the student route and identifies where a request terminates '
                'without creating a record. The ERD shows where each accepted enrollment is stored.')],
  'links': []},
 {'id': 'vlip',
  'name': 'VLIP',
  'type': 'Vancouver Local Immigration Partnership · Redesign',
  'category': 'client',
  'tags': [],
  'summary': 'A homepage redesign for a Vancouver partnership supporting newcomer inclusion.',
  'image': 'vlip',
  'image_caption': 'Vancouver shoreline image used in the VLIP homepage prototype.',
  'direct': 'https://jillnguyen2311.github.io/vlip-page/'},
 {'id': 'nikato',
  'name': 'Nikato Landscape',
  'type': 'Small business · Customer journey',
  'category': 'client',
  'tags': [],
  'summary': 'A landscaping service website with service information and a quote request path.',
  'image': 'nikato',
  'image_caption': 'Landscaping image from the rebuilt Nikato website.',
  'direct': 'https://jillnguyen2311.github.io/nikato-landscape/'},
 {'id': 'syndicate',
  'name': 'Syndicate AI',
  'type': 'Business case · Launch planning',
  'category': 'systems',
  'role': 'Business case and launch analysis',
  'when': '2024',
  'status': 'Proposed venture',
  'tags': ['Market analysis', 'Operations', 'Financial assumptions', 'Risk'],
  'summary': 'Evaluated an AI integration venture and used market, operations, finance and risk analysis to '
             'shape launch requirements.',
  'cover': ['Market', 'Operating model', 'Financial assumptions', 'Risks'],
  'sections': [('Business question',
                'The proposed venture would help businesses adopt AI through integration and advisory '
                'services. The planning question was what it would take to offer and support those services.'),
               ('Feasibility analysis',
                'I contributed to a business plan covering market segments, positioning, service delivery, '
                'operations, marketing and sales, staffing, finance and risk. The plan explored a subscription '
                'model and considered how technology change and competition could affect delivery.'),
               ('Launch requirements',
                'The business case linked the target customer and service offer to the operating capabilities '
                'and financial assumptions needed to plan the launch. The outcome was a business plan and '
                'pitch for a proposed venture.'),
               ('Where the analysis informs a decision',
                'Positioning and customer selection define who needs the service. The operating model '
                'specifies the staffing and support needed to deliver it. Financial assumptions test whether '
                'recurring revenue can support the service. Risks such as fast-moving technology or '
                'competition become assumptions to revisit before committing to launch.')],
  'links': []},
 {'id': 'whitestone',
  'name': 'WhiteStone',
  'type': 'BCIT · Product prototype',
  'category': 'product',
  'role': 'UI/UX Designer and Front-end Developer',
  'when': '2023',
  'status': 'Team prototype',
  'tags': ['Personas', 'Requirements', 'Figma', 'Next.js'],
  'summary': 'A BCIT team prototype that turns an oral-health scan result into severity information and '
             'supporting resources.',
  'image': 'whitestone',
  'image_caption': 'WhiteStone product mockups from the team design exports.',
  'sections': [('What the team set out to build',
                'WhiteStone was a student prototype for communicating oral-health screening findings. A user '
                'needed to understand their results and find helpful reading without having to interpret the '
                'raw output.'),
               ('My design and implementation contribution',
                'I used team personas and wireframes to work through the results experience, including '
                'grouping findings by severity and giving users a path from a finding to related resources. I '
                'built the results flow and Health Resources components in Next.js and contributed to the '
                'prototype presentation.'),
               ('From component to prototype',
                'The gallery shows the shared components, wireframe alternatives and high-fidelity work that '
                'guided implementation. For the results interface, labelled severity states give a finding a '
                'readable status and the resource section provides a follow-up path.')],
  'live': 'https://whitestone-idsp.vercel.app/',
  'links': [('WhiteStone team repository', 'https://github.com/WhiteStoneDental/whitestone_IDSP')]},
 {'id': 'heathelp',
  'name': 'HeatHelp',
  'type': 'Product prototype · Learning flows',
  'category': 'product',
  'role': 'UI/UX Designer and Front-end Developer',
  'when': 'BCIT project',
  'status': 'Team prototype',
  'tags': ['User flows', 'State modelling', 'Component guide'],
  'summary': 'A team-designed fire safety learning prototype with topic-based learning, quizzes and a progress '
             'indicator.',
  'image': 'heathelp',
  'image_caption': 'HeatHelp interface mockups from the team design exports.',
  'sections': [('Learning and quiz experience',
                'HeatHelp organizes short learning content and quizzes by topic. My team defined the entry '
                'points for learning and testing, the sequence of questions and the progress states. We used '
                'low- and high-fidelity designs to refine the flow.'),
               ('Prototype and feedback',
                'Team usability notes reported that Learn More and Quiz looked similar, that users could lose '
                'their way in navigation, and that one participant expected a broader quiz. Those observations '
                'point to clearer destinations and quiz scope in the UI.'),
               ('Shared interaction patterns',
                'The progress indicator and reusable buttons give students a consistent sense of what comes '
                'next. The prototype screens show how those components fit into the completed flows.')],
  'live': 'https://heathelp.vercel.app/',
  'links': []},
 {'id': 'westernstains',
  'name': 'WesternStains',
  'type': 'Client project · E-commerce',
  'category': 'client',
  'role': 'Client discovery and Shopify delivery',
  'when': '2024',
  'status': 'Archived storefront',
  'tags': ['Requirements elicitation', 'Product taxonomy', 'Shopify'],
  'summary': 'Gathered client requirements and structured a Shopify store around how customers choose and '
             'purchase wood oils.',
  'cover': ['Surface', 'Application', 'Product selection'],
  'sections': [('Client need',
                'The client needed a storefront that could explain and sell wood oils. Customers needed enough '
                'information to select a suitable product for the surface and application.'),
               ('Requirements and information architecture',
                'I gathered client requirements and organized collections, product pages and buying guides '
                'around the customer’s comparison process.'),
               ('Delivery',
                'I built the Shopify storefront so customers could browse the product range, consult buying '
                'guidance and purchase on the same site.'),
               ('Merchandising requirements',
                'I structured collections to support selection by surface and application, then used product '
                'pages and buying guidance to connect a customer’s intended use to suitable products. The '
                'storefront brought comparison and purchase into the same path.')],
  'links': []},
 {'id': 'weather',
  'name': 'Weather App',
  'type': 'BCIT · API integration',
  'category': 'engineering',
  'role': 'Front-end and API implementation',
  'when': '2024',
  'status': 'Course project',
  'tags': ['API mapping', 'Error handling', 'TypeScript'],
  'summary': 'Mapped a location query to weather data and implemented current conditions, forecasts and '
             'failed-request handling.',
  'cover': ['Location', 'OpenWeatherMap', 'Weather + forecast'],
  'sections': [('Data requirement',
                'Users needed current conditions and a five-day forecast for their location. The interface had '
                'to translate the location query into a request and map the response to readable weather '
                'data.'),
               ('Integration and failure states',
                'I integrated OpenWeatherMap in Next.js and TypeScript using Fetch and Axios, and implemented '
                'how the application handles failed requests.')],
  'links': [('Source repository', 'https://github.com/jillnguyen2311/weather-app-2024')]},
 {'id': 'elib360',
  'name': 'eLib360',
  'type': 'BachKhoaTech · Digital library',
  'category': 'systems',
  'role': 'Information architecture and scope definition',
  'when': '2025',
  'status': 'Concept and requirements',
  'tags': ['Taxonomy', 'Scope definition', 'Access requirements'],
  'summary': 'Discovery, filter dependencies and access requirements for a shared digital learning library.',
  'cover': ['K–12', 'Higher education', 'Research'],
  'sections': [('The library problem',
                'Students, educators and researchers need one place to find textbooks, lectures, assessments, '
                'interactive materials and research. The specification groups these into material types and '
                'education levels, with interactive learning and simulation linked to LMS360.'),
               ('Search and filter behaviour',
                'Advanced search uses curriculum, level and subject. Subject and textbook series depend on the '
                'selected curriculum. The draft defaults to the new curriculum; changing curriculum means '
                'dependent choices must be re-evaluated.'),
               ('Access and release scope',
                'The design covers public community materials and school-only materials requiring school '
                'sign-in. The scoped plan distinguishes users with school-issued accounts from a later '
                'self-registration track, with different review requirements for community uploads.'),
               ('Rules to verify',
                'Change curriculum and verify the eligible subjects and series change. Attempt to open a '
                'school-only asset without the correct sign-in. Follow a linked interactive learning asset '
                'through to the learning platform.')]},
 {'id': 'lms360',
  'name': 'LMS360',
  'type': 'BachKhoaTech · Learning platform',
  'category': 'systems',
  'role': 'Workflow and requirements analysis',
  'when': 'BachKhoaTech',
  'status': 'Product and scoped requirements',
  'tags': ['Workflow', 'Placement rules', 'Content handoff'],
  'summary': 'Teacher and learner workflows for speaking practice, plus placement requirements for admissions campaigns.',
  'cover': ['Campaign request', 'Placement rules', 'Admissions landing page'],
  'sections': [('The business problem',
                'The learning platform needed a clear way to surface admissions and scholarship information. A '
                'placement in the learning platform and the landing page that explains the offer have distinct '
                'content needs.'),
               ('Workflow and business rules',
                'The proposal describes requests for campaign placement, platform areas such as the homepage '
                'and resource screens, and destinations for offers or scholarships. Placement types include '
                'header banners, side banners and pop-ups. The requirements distinguish desktop and mobile '
                'specifications.'),
               ('Handoff and validation',
                'The design establishes which placement appears on each product surface and where it leads. '
                'Verification can compare the approved placement, desktop and mobile rendering and the '
                'intended destination against the request.')],
  'links': [('LMS360 platform', 'https://lms360.vn/')]},
 {'id': 'test360',
  'name': 'TEST360',
  'type': 'BachKhoaTech · Digital assessment',
  'category': 'systems',
  'role': 'Assessment product design contribution',
  'when': 'BachKhoaTech',
  'status': 'Product design',
  'tags': ['Workflow modelling', 'Data mapping', 'Prototyping'],
  'summary': 'Teacher assessment and score synchronization design, including how users review the selected '
             'destination and converted results.',
  'cover': ['Assessment setup', 'Learner attempt', 'Results review'],
  'sections': [('What the design covers',
                'TEST360 supports digital assessment in the 360 suite. The Figma page contains a '
                'grading-session setup dialog, speaking-assessment screens, student performance details and a '
                'teacher score synchronization flow.'),
               ('A worked example · Score synchronization',
                'In the score-review dialog, the teacher chooses academic term, target grade column and '
                'subject. They also choose a score-selection method and rounding. The table presents the '
                'source and converted score together so the teacher can review the mapping before '
                'synchronizing.'),
               ('Requirements that follow from the screen',
                'Treat the term, subject and grade column as destination inputs. Make the conversion choices '
                'visible beside the results, then confirm the selected mapping before proceeding. In a '
                'validation example, compare the source and converted columns and verify that a change to '
                'rounding is reflected in the preview.')]}]

ARCHIVE = [('NBA Tracker', 'API-backed sports information', 'NBATracker-final-project-MDIA3109'),
 ('Expo and Millennium Line Map',
  'Transit route mapping and information display',
  'Expo-Line-and-Millennium-Line'),
 ('Recipe App', 'Recipe data and full-stack integration', 'recipe-app-fullstack'),
 ('Task Management App', 'Task workflows and state handling', 'task-management-app'),
 ('Timed To-dos', 'Time-based task interactions', 'task-management-app-timed-todos'),
 ('NASA EPIC', 'External image data and UI rendering', 'class5-nasa-api-nextjs'),
 ('Firebase Lab', 'Firebase integration in an Expo course project', 'lab2-assignment-firebase'),
 ('Cypress Assessment', 'Browser-based test automation', 'assessment1-cypress'),
 ('Playwright Testing', 'Browser test scenarios', 'Class5-PlaywrightUnitTesting'),
 ('Food Gallery Website', 'Team web project and content presentation', 'food-gallery-website-group-pj'),
 ('Website Translation', 'Multilingual page behaviour', 'website-translation-asm'),
 ('UI Library', 'Reusable interface components', 'ui-library'),
 ('Spine 3D', 'Interactive development study', 'spine-3d'),
 ('Dynamic Content Project', 'Data-driven page rendering', 'DynamicContent-Assignment1-project'),
 ('ChartKit UI', 'Mobile data visualization study', 'chartkitui-expo'),
 ('News Feed App', 'React interface and item interactions', 'newsfeedapp-lab2-delbtn-updated')]

DESIGN = [('Bunana', 'Beverage packaging concept and visual identity', 'bunana'),
 ('Think Before Getting a Bunny', 'Animated information video about pet ownership', 'bunny-video'),
 ('Camera Digital Drawing', 'Digital illustration of a Polaroid camera', 'camera-drawing')]

DESIGN_DETAILS = {'bunana': 'A visual identity and beverage-can packaging concept. The artwork demonstrates the relationship '
           'between the front label, colour treatment and brand presentation.',
 'bunny-video': 'I illustrated and animated this short video to explain what it takes to care for a rabbit. The story follows a rabbit given as a gift and asks viewers to consider the commitment before bringing one home.',
 'camera-drawing': 'A digital study of a Polaroid-style camera. The composition uses shape, texture and small '
                   'details to communicate the character of the object.'}
