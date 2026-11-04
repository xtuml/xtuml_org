---
redirect_from:
  - "/community/topic/compiled-c-crash-on-escher_classfactoryinit/"

layout: "topic"
title: "Compiled C crash on Escher_ClassFactoryInit"
date: "2024-02-09"
permalink: "/forums/topic/compiled-c-crash-on-escher_classfactoryinit/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Schmill** · February 9, 2024 at 9:59 am

Hi there,
This may be impossible to answer, but perhaps it is a known issue with a workaround:

While the verifier works fine, the compiled C executable (windows) crashes when it reaches the `dci->active.head = 0;` line in the `Escher_ClassFactoryInit ` function.
I post bellow the malicious class .xtuml in case it is helpful.

Thank you.

— BP 7.1.6 content: ModelClass syschar: 3 persistence-version: 7.1.6

INSERT INTO O_OBJ
VALUES (“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195″,
‘REQUEST’,
2,
‘REQ’,
”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO O_NBATTR
VALUES (“c348d53f-ffb0-426b-89d8-42c0948f381d”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_BATTR
VALUES (“c348d53f-ffb0-426b-89d8-42c0948f381d”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_ATTR
VALUES (“c348d53f-ffb0-426b-89d8-42c0948f381d”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”,
“2c3de273-ec5d-4397-82a2-7e4a51561b7c”,
‘RequestID’,
”,
”,
‘RequestID’,
0,
“ba5eda7a-def5-0000-0000-000000000005″,
”,
”);
INSERT INTO O_NBATTR
VALUES (“7e60e836-795e-4152-954e-0e0fc067e9e9”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_BATTR
VALUES (“7e60e836-795e-4152-954e-0e0fc067e9e9”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_ATTR
VALUES (“7e60e836-795e-4152-954e-0e0fc067e9e9”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”,
“c348d53f-ffb0-426b-89d8-42c0948f381d”,
‘CreatedComposite’,
”,
”,
‘CreatedComposite’,
0,
“ba5eda7a-def5-0000-0000-000000000005″,
”,
”);
INSERT INTO O_NBATTR
VALUES (“0550c338-9307-4882-92cc-ef6ff5e7eca2”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_BATTR
VALUES (“0550c338-9307-4882-92cc-ef6ff5e7eca2”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_ATTR
VALUES (“0550c338-9307-4882-92cc-ef6ff5e7eca2”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”,
“7e60e836-795e-4152-954e-0e0fc067e9e9″,
‘current_state’,
”,
”,
‘current_state’,
0,
“ba5eda7a-def5-0000-0000-000000000006″,
”,
”);
INSERT INTO O_NBATTR
VALUES (“2c3de273-ec5d-4397-82a2-7e4a51561b7c”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_BATTR
VALUES (“2c3de273-ec5d-4397-82a2-7e4a51561b7c”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_ATTR
VALUES (“2c3de273-ec5d-4397-82a2-7e4a51561b7c”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”,
“00000000-0000-0000-0000-000000000000″,
‘TestRequestId’,
”,
”,
‘TestRequestId’,
0,
“ba5eda7a-def5-0000-0000-000000000005″,
”,
”);
INSERT INTO O_ID
VALUES (0,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_OIDA
VALUES (“2c3de273-ec5d-4397-82a2-7e4a51561b7c”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”,
0,
‘TestRequestId’);
INSERT INTO O_ID
VALUES (1,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO O_ID
VALUES (2,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO PE_PE
VALUES (“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”,
1,
“45bff065-3958-4b70-8610-0e77b17e859d”,
“00000000-0000-0000-0000-000000000000”,
4);
INSERT INTO EP_PKG_PROXY
VALUES (“45bff065-3958-4b70-8610-0e77b17e859d”,
“00000000-0000-0000-0000-000000000000”,
“703d9746-6e19-4719-96eb-4aa92f1631c6″,
‘Information’,
”,
0,
‘../Information.xtuml’);

—————————————————————————————————————
—————————————————————————————————————
———————————————-Instance State Machine—————————————-
—————————————————————————————————————
—————————————————————————————————————
— BP 7.1.6 content: InstanceStateMachine syschar: 3 persistence-version: 7.1.6

INSERT INTO SM_ISM
VALUES (“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195”);
INSERT INTO SM_SM
VALUES (“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
”,
0);
INSERT INTO SM_MOORE
VALUES (“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”);
INSERT INTO SM_EVTDI
VALUES (“8c130496-5be7-4c27-8d72-d4542a9dbe6e”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
‘composite’,
”,
“ba5eda7a-def5-0000-0000-000000000005″,
”,
“1617a910-364a-4f09-a010-e3ea38c2c5e0”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO SM_LEVT
VALUES (“1617a910-364a-4f09-a010-e3ea38c2c5e0”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO SM_SEVT
VALUES (“1617a910-364a-4f09-a010-e3ea38c2c5e0”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO SM_EVT
VALUES (“1617a910-364a-4f09-a010-e3ea38c2c5e0”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“00000000-0000-0000-0000-000000000000″,
1,
‘complete’,
0,
”,
‘REQ1’,
”);
INSERT INTO SM_STATE
VALUES (“c568e76e-ea16-4b59-9d3c-726420c55734”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“00000000-0000-0000-0000-000000000000”,
‘Created’,
1,
0);
INSERT INTO SM_SEME
VALUES (“c568e76e-ea16-4b59-9d3c-726420c55734”,
“1617a910-364a-4f09-a010-e3ea38c2c5e0”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO SM_STATE
VALUES (“4676257f-460f-4554-b84b-654b9c20c54b”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“00000000-0000-0000-0000-000000000000”,
‘Completing’,
2,
0);
INSERT INTO SM_CH
VALUES (“4676257f-460f-4554-b84b-654b9c20c54b”,
“1617a910-364a-4f09-a010-e3ea38c2c5e0”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“00000000-0000-0000-0000-000000000000″,
”);
INSERT INTO SM_SEME
VALUES (“4676257f-460f-4554-b84b-654b9c20c54b”,
“1617a910-364a-4f09-a010-e3ea38c2c5e0”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO SM_NSTXN
VALUES (“9b63c915-45ad-4a95-8baf-e8b0ef3f2be3”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“c568e76e-ea16-4b59-9d3c-726420c55734”,
“1617a910-364a-4f09-a010-e3ea38c2c5e0”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO SM_TXN
VALUES (“9b63c915-45ad-4a95-8baf-e8b0ef3f2be3”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“4676257f-460f-4554-b84b-654b9c20c54b”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO SM_MOAH
VALUES (“cc100f52-b0b4-4c76-9985-78fa24d5cb2c”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“c568e76e-ea16-4b59-9d3c-726420c55734”);
INSERT INTO SM_AH
VALUES (“cc100f52-b0b4-4c76-9985-78fa24d5cb2c”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”);
INSERT INTO SM_ACT
VALUES (“cc100f52-b0b4-4c76-9985-78fa24d5cb2c”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
1,
”,
”,
0);
INSERT INTO SM_MOAH
VALUES (“73fb572a-77ca-4f1b-8cfb-7e291deccf22”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“4676257f-460f-4554-b84b-654b9c20c54b”);
INSERT INTO SM_AH
VALUES (“73fb572a-77ca-4f1b-8cfb-7e291deccf22”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”);
INSERT INTO SM_ACT
VALUES (“73fb572a-77ca-4f1b-8cfb-7e291deccf22”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
1,
‘assign self.CreatedComposite = param.composite;
select one test related by self-\>TEST\[R1.”is sent by”\];
unrelate self from test across R1.”is sent by”;
generate TEST2:requestComplete() to test;’,
”,
0);
INSERT INTO SM_TAH
VALUES (“e51759ce-7c47-4161-8e9d-40ad078dd294”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
“9b63c915-45ad-4a95-8baf-e8b0ef3f2be3”);
INSERT INTO SM_AH
VALUES (“e51759ce-7c47-4161-8e9d-40ad078dd294”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”);
INSERT INTO SM_ACT
VALUES (“e51759ce-7c47-4161-8e9d-40ad078dd294”,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
1,
”,
”,
0);
INSERT INTO GD_MD
VALUES (“ac3a9959-267e-4750-b773-cbf9ad04dc58”,
8,
“d1faf1f2-f3f3-4d22-bbd4-6eef4d14e0cc”,
40,
0,
0,
1,
1,
1,
12,
1,
0,
0,
0,
0,
0,
‘4.1.17’,
‘umltools::Domin::VER::Multi Requests::Information::REQUEST::Instance State Machine’);
INSERT INTO GD_GE
VALUES (“251c4f8b-3e1a-4290-b43a-361792223c41”,
“ac3a9959-267e-4750-b773-cbf9ad04dc58”,
“c568e76e-ea16-4b59-9d3c-726420c55734”,
41,
0,
‘umltools::Domin::VER::Multi Requests::Information::REQUEST::Instance State Machine::Created’);
INSERT INTO GD_SHP
VALUES (“251c4f8b-3e1a-4290-b43a-361792223c41”);
INSERT INTO GD_NCS
VALUES (“251c4f8b-3e1a-4290-b43a-361792223c41”);
INSERT INTO DIM_ND
VALUES (301.000000,
73.000000,
“251c4f8b-3e1a-4290-b43a-361792223c41”);
INSERT INTO DIM_GE
VALUES (4308.000000,
3264.000000,
“251c4f8b-3e1a-4290-b43a-361792223c41”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_ELE
VALUES (“251c4f8b-3e1a-4290-b43a-361792223c41”,
0,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_CON
VALUES (“85ab4fb5-4e8a-4fa2-b33f-dc1033fac9de”,
4464.000000,
3337.000000,
“251c4f8b-3e1a-4290-b43a-361792223c41”);
INSERT INTO GD_GE
VALUES (“9cd8e9b0-bc11-4093-b282-3c005cbe3be9”,
“ac3a9959-267e-4750-b773-cbf9ad04dc58”,
“4676257f-460f-4554-b84b-654b9c20c54b”,
41,
0,
‘umltools::Domin::VER::Multi Requests::Information::REQUEST::Instance State Machine::Completing’);
INSERT INTO GD_SHP
VALUES (“9cd8e9b0-bc11-4093-b282-3c005cbe3be9”);
INSERT INTO GD_NCS
VALUES (“9cd8e9b0-bc11-4093-b282-3c005cbe3be9”);
INSERT INTO DIM_ND
VALUES (409.000000,
144.000000,
“9cd8e9b0-bc11-4093-b282-3c005cbe3be9”);
INSERT INTO DIM_GE
VALUES (4308.000000,
3408.000000,
“9cd8e9b0-bc11-4093-b282-3c005cbe3be9”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_ELE
VALUES (“9cd8e9b0-bc11-4093-b282-3c005cbe3be9”,
0,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_CON
VALUES (“8b33af27-66db-46fa-813c-4cd0806076f2”,
4464.000000,
3408.000000,
“9cd8e9b0-bc11-4093-b282-3c005cbe3be9”);
INSERT INTO GD_GE
VALUES (“159ac436-ad65-4d99-af92-1092e03acf99”,
“ac3a9959-267e-4750-b773-cbf9ad04dc58”,
“9b63c915-45ad-4a95-8baf-e8b0ef3f2be3”,
42,
0,
‘umltools::Domin::VER::Multi Requests::Information::REQUEST::Instance State Machine::Created::REQ1: complete’);
INSERT INTO GD_CON
VALUES (“159ac436-ad65-4d99-af92-1092e03acf99”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO GD_CTXT
VALUES (“ac5166a9-4c20-4d8e-8e41-d6f86fd5d82e”,
“159ac436-ad65-4d99-af92-1092e03acf99”,
0,
0.000000,
0.000000);
INSERT INTO DIM_ND
VALUES (0.000000,
0.000000,
“ac5166a9-4c20-4d8e-8e41-d6f86fd5d82e”);
INSERT INTO DIM_GE
VALUES (0.000000,
0.000000,
“ac5166a9-4c20-4d8e-8e41-d6f86fd5d82e”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_ELE
VALUES (“ac5166a9-4c20-4d8e-8e41-d6f86fd5d82e”,
0,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO GD_CTXT
VALUES (“a56dadcd-9ab4-4e0c-8260-8e3f31ea1c14”,
“159ac436-ad65-4d99-af92-1092e03acf99”,
2,
0.000000,
0.000000);
INSERT INTO DIM_ND
VALUES (0.000000,
0.000000,
“a56dadcd-9ab4-4e0c-8260-8e3f31ea1c14”);
INSERT INTO DIM_GE
VALUES (4268.000000,
3366.000000,
“a56dadcd-9ab4-4e0c-8260-8e3f31ea1c14”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_ELE
VALUES (“a56dadcd-9ab4-4e0c-8260-8e3f31ea1c14”,
0,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO GD_CTXT
VALUES (“e90799ef-1caa-414a-99e3-cc11cda14d69”,
“159ac436-ad65-4d99-af92-1092e03acf99”,
1,
0.000000,
0.000000);
INSERT INTO DIM_ND
VALUES (0.000000,
0.000000,
“e90799ef-1caa-414a-99e3-cc11cda14d69”);
INSERT INTO DIM_GE
VALUES (0.000000,
0.000000,
“e90799ef-1caa-414a-99e3-cc11cda14d69”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_ELE
VALUES (“e90799ef-1caa-414a-99e3-cc11cda14d69”,
0,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO GD_LS
VALUES (“d0bf86c3-ff48-49dc-a928-a0157b8fcdfc”,
“159ac436-ad65-4d99-af92-1092e03acf99”,
“00000000-0000-0000-0000-000000000000”,
“7d649b9a-72db-4d3a-840f-b239d9d751c6”,
“e55aaa27-ea03-48ec-90e2-7a533b19e4ef”);
INSERT INTO DIM_WAY
VALUES (“7d649b9a-72db-4d3a-840f-b239d9d751c6”,
4464.000000,
3337.000000,
“159ac436-ad65-4d99-af92-1092e03acf99”,
“00000000-0000-0000-0000-000000000000”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_WAY
VALUES (“e55aaa27-ea03-48ec-90e2-7a533b19e4ef”,
4464.000000,
3408.000000,
“159ac436-ad65-4d99-af92-1092e03acf99”,
“00000000-0000-0000-0000-000000000000”,
“7d649b9a-72db-4d3a-840f-b239d9d751c6”);
INSERT INTO DIM_GE
VALUES (0.000000,
0.000000,
“159ac436-ad65-4d99-af92-1092e03acf99”,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_ELE
VALUES (“159ac436-ad65-4d99-af92-1092e03acf99”,
0,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO DIM_ED
VALUES (“85ab4fb5-4e8a-4fa2-b33f-dc1033fac9de”,
“8b33af27-66db-46fa-813c-4cd0806076f2”,
“159ac436-ad65-4d99-af92-1092e03acf99”);
INSERT INTO DIM_DIA
VALUES (“ac3a9959-267e-4750-b773-cbf9ad04dc58″,
”,
1.000000,
0.000000,
0.000000,
“00000000-0000-0000-0000-000000000000”);
INSERT INTO O_OBJ_PROXY
VALUES (“6bcbcac6-f416-41c8-90bc-4dcc8cfe9195″,
‘REQUEST’,
2,
‘REQ’,
”,
“00000000-0000-0000-0000-000000000000”,
‘../REQUEST.xtuml’);

---

**cort** · February 9, 2024 at 12:12 pm

One difference between Verifier and MC-3020 is that Verifier defaults to dynamic memory allocation. In MC-3020 you must mark your instance population sizes. They default to 10.
Could this be the issue?

---

**Schmill** · February 9, 2024 at 1:52 pm

I have dynamic memory allocation enabled; I have now also tried to increase the extent size but unfortunately it still crashes on startup.
