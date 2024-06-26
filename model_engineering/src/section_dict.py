# SECTION A: DEMOGRAPHICS, IDENTIFIERS, AND WEIGHTS (253 features)
# Person Specific Identifier
Demog1=['unhhid','cunicah','codent01','codent03','ps3','ent2','np','unhhidnp','rahhidnp','tipent_01','tipent_03','tipent_12','tipent_15','tipent_18']
# Household Identifier
Demog2=['h1hhid', 'h2hhid', 'h3hhid', 'h4hhid', 'h5hhid', 'h1hhidc', 'h2hhidc', 'h3hhidc', 'h4hhidc', 'h5hhidc', 'acthog', 'subhog_01', 'subhog_03', 'subhog_12', 'subhog_15', 'subhog_18']
# Spouse Identifier
Demog3=['s1hhidnp', 's2hhidnp', 's3hhidnp', 's4hhidnp', 's5hhidnp']
# Wave Status: Response Indicator
Demog4=['inw1', 'inw2', 'inw3', 'inw4', 'inw5']
# Wave Status: Interview Status
Demog5=['r1iwstat', 'r2iwstat', 'r3iwstat', 'r4iwstat', 'r5iwstat', 's1iwstat', 's2iwstat', 's3iwstat', 's4iwstat', 's5iwstat']
# Sample Cohort
Demog6=['hacohort']
# Whether Proxy Interview
Demog7=['r1proxy', 'r2proxy', 'r3proxy', 'r4proxy', 'r5proxy', 's1proxy', 's2proxy', 's3proxy', 's4proxy', 's5proxy']
# Number of Household Respondents
Demog8=['h1hhresp', 'h2hhresp', 'h3hhresp', 'h4hhresp', 'h5hhresp']
# Whether Couple Household
Demog9=['h1cpl', 'h2cpl', 'h3cpl', 'h4cpl', 'h5cpl']
# Household Analysis Weight
Demog10=['r1wthh', 'r2wthh', 'r3wthh', 'r4wthh', 'r5wthh']
# Person-Level Analysis Weight
Demog11=['r1wtresp', 'r2wtresp', 'r3wtresp', 'r4wtresp', 'r5wtresp', 's1wtresp', 's2wtresp', 's3wtresp', 's4wtresp', 's5wtresp']
# Interview Dates
Demog12=['r1iwm', 'r2iwm', 'r3iwm', 'r4iwm', 'r5iwm', 's1iwm', 's2iwm', 's3iwm', 's4iwm', 's5iwm', 'r1iwy', 'r2iwy', 'r3iwy', 'r4iwy', 'r5iwy', 's1iwy', 's2iwy', 's3iwy', 's4iwy', 's5iwy', 'r1iwf', 'r2iwf', 'r3iwf', 'r4iwf', 'r5iwf', 's1iwf', 's2iwf', 's3iwf', 's4iwf', 's5iwf']
# Birth Date: Month and Year
Demog13=['rabyear', 's1byear', 's2byear', 's3byear', 's4byear', 's5byear', 'rabmonth', 's1bmonth', 's2bmonth', 's3bmonth', 's4bmonth', 's5bmonth']
# Death Date: Month and Year
Demog14=['radyear', 's1dyear', 's2dyear', 's3dyear', 's4dyear', 's5dyear', 'radmonth', 's1dmonth', 's2dmonth', 's3dmonth', 's4dmonth', 's5dmonth']
# Age at Interview (Months and Years)
Demog15=['r1agey', 'r2agey', 'r3agey', 'r4agey', 'r5agey', 's1agey', 's2agey', 's3agey', 's4agey', 's5agey']
# Gender
Demog16=['ragender', 's1gender', 's2gender', 's3gender', 's4gender', 's5gender', 'r2genderf', 'r3genderf', 'r4genderf', 'r5genderf', 's2genderf', 's3genderf', 's4genderf', 's5genderf']
# Education
Demog17=['raedyrs', 's1edyrs', 's2edyrs', 's3edyrs', 's4edyrs', 's5edyrs']
# Education: Categories by ISCED Codes
Demog18=['raedisced', 's1edisced', 's2edisced', 's3edisced', 's4edisced', 's5edisced']
# Education: Harmonized Education
Demog19=['raeducl', 's1educl', 's2educl', 's3educl', 's4educl', 's5educl']
# Literacy and Numeracy
Demog20=['raliterate', 's1literate', 's2literate', 's3literate', 's4literate', 's5literate', 'ranumerate', 's1numerate', 's2numerate', 's3numerate', 's4numerate', 's5numerate']
# Indigenous Language
Demog21=['raindlang', 's1indlang', 's3indlang', 's4indlang', 's5indlang']
# Current Marital Status: Current Partnership Status
Demog22=['r1mpart', 'r2mpart', 'r3mpart', 'r4mpart', 'r5mpart', 's1mpart', 's2mpart', 's3mpart', 's4mpart', 's5mpart']
# Current Marital Status: With Partnership
Demog23=['r1mstat', 'r2mstat', 'r3mstat', 'r4mstat', 'r5mstat', 's1mstat', 's2mstat', 's3mstat', 's4mstat', 's5mstat']
# Current Marital Status: Without Partnership
Demog24=['r1mstath', 'r2mstath', 'r3mstath', 'r4mstath', 'r5mstath', 's1mstath', 's2mstath', 's3mstath', 's4mstath', 's5mstath']
# Number of Marriages
Demog25=['r1mrct', 'r2mrct', 'r3mrct', 'r4mrct', 'r5mrct', 's1mrct', 's2mrct', 's3mrct', 's4mrct', 's5mrct']
# Urban or Rural
Demog26=['h1rural', 'h3rural', 'h4rural', 'h5rural', 'h1rural_m', 'h3rural_m', 'h4rural_m', 'h5rural_m']

# SECTION B: HEALTH (1624 features)
# Self-Report of Health
Health1 =['r1shlt', 'r2shlt', 'r3shlt', 'r4shlt', 'r5shlt', 's1shlt', 's2shlt', 's3shlt', 's4shlt', 's5shlt','r1hltc', 'r2hltc', 'r3hltc', 'r4hltc', 'r5hltc', 's1hltc', 's2hltc', 's3hltc', 's4hltc', 's5hltc']
# Activities of Daily Living (ADLs): Raw Recodes
Health2 = ['r1dress', 'r2dress', 'r3dress', 'r4dress', 'r5dress', 's1dress', 's2dress', 's3dress', 's4dress', 's5dress', 'r1walkr', 'r2walkr', 'r3walkr', 'r4walkr', 'r5walkr', 's1walkr', 's2walkr', 's3walkr', 's4walkr', 's5walkr', 'r1bath', 'r2bath', 'r3bath', 'r4bath', 'r5bath', 's1bath', 's2bath', 's3bath', 's4bath', 's5bath', 'r1eat', 'r2eat', 'r3eat', 'r4eat', 'r5eat', 's1eat', 's2eat', 's3eat', 's4eat', 's5eat', 'r1bed', 'r2bed', 'r3bed', 'r4bed', 'r5bed', 's1bed', 's2bed', 's3bed', 's4bed', 's5bed', 'r1toilt', 'r2toilt', 'r3toilt', 'r4toilt', 'r5toilt', 's1toilt', 's2toilt', 's3toilt', 's4toilt', 's5toilt']
# Activities of Daily Living (ADLs): Some Difficulty
Health3 = ['r1walkra', 'r2walkra', 'r3walkra', 'r4walkra', 'r5walkra', 's1walkra', 's2walkra', 's3walkra', 's4walkra', 's5walkra', 'r1dressa', 'r2dressa', 'r3dressa', 'r4dressa', 'r5dressa', 's1dressa', 's2dressa', 's3dressa', 's4dressa', 's5dressa', 'r1batha', 'r2batha', 'r3batha', 'r4batha', 'r5batha', 's1batha', 's2batha', 's3batha', 's4batha', 's5batha', 'r1eata', 'r2eata', 'r3eata', 'r4eata', 'r5eata', 's1eata', 's2eata', 's3eata', 's4eata', 's5eata', 'r1beda', 'r2beda', 'r3beda', 'r4beda', 'r5beda', 's1beda', 's2beda', 's3beda', 's4beda', 's5beda', 'r1toilta', 'r2toilta', 'r3toilta', 'r4toilta', 'r5toilta', 's1toilta', 's2toilta', 's3toilta', 's4toilta', 's5toilta']
# Instrumental Activities of Daily Living (IADLs): Raw Recodes
Health4 = ['r1money', 'r2money', 'r3money', 'r4money', 'r5money', 's1money', 's2money', 's3money', 's4money', 's5money', 'r1meds', 'r2meds', 'r3meds', 'r4meds', 'r5meds', 's1meds', 's2meds', 's3meds', 's4meds', 's5meds', 'r1shop', 'r2shop', 'r3shop', 'r4shop', 'r5shop', 's1shop', 's2shop', 's3shop', 's4shop', 's5shop', 'r1meals', 'r2meals', 'r3meals', 'r4meals', 'r5meals', 's1meals', 's2meals', 's3meals', 's4meals', 's5meals']
# Instrumental Activities of Daily Living (IADLs): Some Difficulty
Health5 = ['r1moneya', 'r2moneya', 'r3moneya', 'r4moneya', 'r5moneya', 's1moneya', 's2moneya', 's3moneya', 's4moneya', 's5moneya', 'r1medsa', 'r2medsa', 'r3medsa', 'r4medsa', 'r5medsa', 's1medsa', 's2medsa', 's3medsa', 's4medsa', 's5medsa', 'r1shopa', 'r2shopa', 'r3shopa', 'r4shopa', 'r5shopa', 's1shopa', 's2shopa', 's3shopa', 's4shopa', 's5shopa', 'r1mealsa', 'r2mealsa', 'r3mealsa', 'r4mealsa', 'r5mealsa', 's1mealsa', 's2mealsa', 's3mealsa', 's4mealsa', 's5mealsa']
# Other Functional Limitations: Raw Recodes
Health6 = ['r1walks', 'r2walks', 'r3walks', 'r4walks', 'r5walks', 's1walks', 's2walks', 's3walks', 's4walks', 's5walks', 'r1jog', 'r2jog', 'r3jog', 'r4jog', 'r5jog', 's1jog', 's2jog', 's3jog', 's4jog', 's5jog', 'r1walk1', 'r2walk1', 'r3walk1', 'r4walk1', 'r5walk1', 's1walk1', 's2walk1', 's3walk1', 's4walk1', 's5walk1', 'r1sit', 'r2sit', 'r3sit', 'r4sit', 'r5sit', 's1sit', 's2sit', 's3sit', 's4sit', 's5sit', 'r1chair', 'r2chair', 'r3chair', 'r4chair', 'r5chair', 's1chair', 's2chair', 's3chair', 's4chair', 's5chair', 'r1clims', 'r2clims', 'r3clims', 'r4clims', 'r5clims', 's1clims', 's2clims', 's3clims', 's4clims', 's5clims', 'r1clim1', 'r2clim1', 'r3clim1', 'r4clim1', 'r5clim1', 's1clim1', 's2clim1', 's3clim1', 's4clim1', 's5clim1', 'r1stoop', 'r2stoop', 'r3stoop', 'r4stoop', 'r5stoop', 's1stoop', 's2stoop', 's3stoop', 's4stoop', 's5stoop', 'r1lift', 'r2lift', 'r3lift', 'r4lift', 'r5lift', 's1lift', 's2lift', 's3lift', 's4lift', 's5lift', 'r1dime', 'r2dime', 'r3dime', 'r4dime', 'r5dime', 's1dime', 's2dime', 's3dime', 's4dime', 's5dime', 'r1arms', 'r2arms', 'r3arms', 'r4arms', 'r5arms', 's1arms', 's2arms', 's3arms', 's4arms', 's5arms', 'r1push', 'r2push', 'r3push', 'r4push', 'r5push', 's1push', 's2push', 's3push', 's4push', 's5push']
# Other Functional Limitations: Some Difficulty
Health7 = ['r1walksa', 'r2walksa', 'r3walksa', 'r4walksa', 'r5walksa', 's1walksa', 's2walksa', 's3walksa', 's4walksa', 's5walksa', 'r1joga', 'r2joga', 'r3joga', 'r4joga', 'r5joga', 's1joga', 's2joga', 's3joga', 's4joga', 's5joga', 'r1walk1a', 'r2walk1a', 'r3walk1a', 'r4walk1a', 'r5walk1a', 's1walk1a', 's2walk1a', 's3walk1a', 's4walk1a', 's5walk1a', 'r1sita', 'r2sita', 'r3sita', 'r4sita', 'r5sita', 's1sita', 's2sita', 's3sita', 's4sita', 's5sita', 'r1chaira', 'r2chaira', 'r3chaira', 'r4chaira', 'r5chaira', 's1chaira', 's2chaira', 's3chaira', 's4chaira', 's5chaira', 'r1climsa', 'r2climsa', 'r3climsa', 'r4climsa', 'r5climsa', 's1climsa', 's2climsa', 's3climsa', 's4climsa', 's5climsa', 'r1clim1a', 'r2clim1a', 'r3clim1a', 'r4clim1a', 'r5clim1a', 's1clim1a', 's2clim1a', 's3clim1a', 's4clim1a', 's5clim1a', 'r1stoopa', 'r2stoopa', 'r3stoopa', 'r4stoopa', 'r5stoopa', 's1stoopa', 's2stoopa', 's3stoopa', 's4stoopa', 's5stoopa', 'r1lifta', 'r2lifta', 'r3lifta', 'r4lifta', 'r5lifta', 's1lifta', 's2lifta', 's3lifta', 's4lifta', 's5lifta', 'r1dimea', 'r2dimea', 'r3dimea', 'r4dimea', 'r5dimea', 's1dimea', 's2dimea', 's3dimea', 's4dimea', 's5dimea', 'r1armsa', 'r2armsa', 'r3armsa', 'r4armsa', 'r5armsa', 's1armsa', 's2armsa', 's3armsa', 's4armsa', 's5armsa', 'r1pusha', 'r2pusha', 'r3pusha', 'r4pusha', 'r5pusha', 's1pusha', 's2pusha', 's3pusha', 's4pusha', 's5pusha']
# ADL Summary: Sum ADLs Where Respondent Reports Any Difficulty
Health8 = ['r1adltot6', 'r2adltot6', 'r3adltot6', 'r4adltot6', 'r5adltot6', 's1adltot6', 's2adltot6', 's3adltot6', 's4adltot6', 's5adltot6', 'r1adltot6m', 'r2adltot6m', 'r3adltot6m', 'r4adltot6m', 'r5adltot6m', 's1adltot6m', 's2adltot6m', 's3adltot6m', 's4adltot6m', 's5adltot6m', 'r1adltot6a', 'r2adltot6a', 'r3adltot6a', 'r4adltot6a', 'r5adltot6a', 's1adltot6a', 's2adltot6a', 's3adltot6a', 's4adltot6a', 's5adltot6a', 'r1adla', 'r2adla', 'r3adla', 'r4adla', 'r5adla', 's1adla', 's2adla', 's3adla', 's4adla', 's5adla', 'r1adlam', 'r2adlam', 'r3adlam', 'r4adlam', 'r5adlam', 's1adlam', 's2adlam', 's3adlam', 's4adlam', 's5adlam', 'r1adlaa', 'r2adlaa', 'r3adlaa', 'r4adlaa', 'r5adlaa', 's1adlaa', 's2adlaa', 's3adlaa', 's4adlaa', 's5adlaa', 'r1adlfive', 'r2adlfive', 'r3adlfive', 'r4adlfive', 'r5adlfive', 's1adlfive', 's2adlfive', 's3adlfive', 's4adlfive', 's5adlfive', 'r1adlfivem', 'r2adlfivem', 'r3adlfivem', 'r4adlfivem', 'r5adlfivem', 's1adlfivem', 's2adlfivem', 's3adlfivem', 's4adlfivem', 's5adlfivem', 'r1adlfivea', 'r2adlfivea', 'r3adlfivea', 'r4adlfivea', 'r5adlfivea', 's1adlfivea', 's2adlfivea', 's3adlfivea', 's4adlfivea', 's5adlfivea', 'r1adla_m', 'r2adla_m', 'r3adla_m', 'r4adla_m', 'r5adla_m', 's1adla_m', 's2adla_m', 's3adla_m', 's4adla_m', 's5adla_m', 'r1adlam_m', 'r2adlam_m', 'r3adlam_m', 'r4adlam_m', 'r5adlam_m', 's1adlam_m', 's2adlam_m', 's3adlam_m', 's4adlam_m', 's5adlam_m', 'r1adlaa_m', 'r2adlaa_m', 'r3adlaa_m', 'r4adlaa_m', 'r5adlaa_m', 's1adlaa_m', 's2adlaa_m', 's3adlaa_m', 's4adlaa_m', 's5adlaa_m', 'r1adlwa', 'r2adlwa', 'r3adlwa', 'r4adlwa', 'r5adlwa', 's1adlwa', 's2adlwa', 's3adlwa', 's4adlwa', 's5adlwa', 'r1adlwam', 'r2adlwam', 'r3adlwam', 'r4adlwam', 'r5adlwam', 's1adlwam', 's2adlwam', 's3adlwam', 's4adlwam', 's5adlwam', 'r1adlwaa', 'r2adlwaa', 'r3adlwaa', 'r4adlwaa', 'r5adlwaa', 's1adlwaa', 's2adlwaa', 's3adlwaa', 's4adlwaa', 's5adlwaa']
# IADL Summary: Sum IADLs Where Respondent Reports Any Difficulty
Health9 = ['r1iadlfour', 'r2iadlfour', 'r3iadlfour', 'r4iadlfour', 'r5iadlfour', 's1iadlfour', 's2iadlfour', 's3iadlfour', 's4iadlfour', 's5iadlfour', 'r1iadlfourm', 'r2iadlfourm', 'r3iadlfourm', 'r4iadlfourm', 'r5iadlfourm', 's1iadlfourm', 's2iadlfourm', 's3iadlfourm', 's4iadlfourm', 's5iadlfourm', 'r1iadlfoura', 'r2iadlfoura', 'r3iadlfoura', 'r4iadlfoura', 'r5iadlfoura', 's1iadlfoura', 's2iadlfoura', 's3iadlfoura', 's4iadlfoura', 's5iadlfoura']
# Other Summary Indices: Mobility, Large Muscle, Gross, Fine Motor, Total, Upper, Lower Body Mobility, and NAGI Activities
Health10 = ['r1mobila', 'r2mobila', 'r3mobila', 'r4mobila', 'r5mobila', 's1mobila', 's2mobila', 's3mobila', 's4mobila', 's5mobila', 'r1mobilam', 'r2mobilam', 'r3mobilam', 'r4mobilam', 'r5mobilam', 's1mobilam', 's2mobilam', 's3mobilam', 's4mobilam', 's5mobilam', 'r1mobilaa', 'r2mobilaa', 'r3mobilaa', 'r4mobilaa', 'r5mobilaa', 's1mobilaa', 's2mobilaa', 's3mobilaa', 's4mobilaa', 's5mobilaa', 'r1lgmusa', 'r2lgmusa', 'r3lgmusa', 'r4lgmusa', 'r5lgmusa', 's1lgmusa', 's2lgmusa', 's3lgmusa', 's4lgmusa', 's5lgmusa', 'r1lgmusam', 'r2lgmusam', 'r3lgmusam', 'r4lgmusam', 'r5lgmusam', 's1lgmusam', 's2lgmusam', 's3lgmusam', 's4lgmusam', 's5lgmusam', 'r1lgmusaa', 'r2lgmusaa', 'r3lgmusaa', 'r4lgmusaa', 'r5lgmusaa', 's1lgmusaa', 's2lgmusaa', 's3lgmusaa', 's4lgmusaa', 's5lgmusaa', 'r1grossa', 'r2grossa', 'r3grossa', 'r4grossa', 'r5grossa', 's1grossa', 's2grossa', 's3grossa', 's4grossa', 's5grossa', 'r1grossam', 'r2grossam', 'r3grossam', 'r4grossam', 'r5grossam', 's1grossam', 's2grossam', 's3grossam', 's4grossam', 's5grossam', 'r1grossaa', 'r2grossaa', 'r3grossaa', 'r4grossaa', 'r5grossaa', 's1grossaa', 's2grossaa', 's3grossaa', 's4grossaa', 's5grossaa', 'r1finea', 'r2finea', 'r3finea', 'r4finea', 'r5finea', 's1finea', 's2finea', 's3finea', 's4finea', 's5finea', 'r1fineam', 'r2fineam', 'r3fineam', 'r4fineam', 'r5fineam', 's1fineam', 's2fineam', 's3fineam', 's4fineam', 's5fineam', 'r1fineaa', 'r2fineaa', 'r3fineaa', 'r4fineaa', 'r5fineaa', 's1fineaa', 's2fineaa', 's3fineaa', 's4fineaa', 's5fineaa', 'r1mobilsev', 'r2mobilsev', 'r3mobilsev', 'r4mobilsev', 'r5mobilsev', 's1mobilsev', 's2mobilsev', 's3mobilsev', 's4mobilsev', 's5mobilsev', 'r1mobilsevm', 'r2mobilsevm', 'r3mobilsevm', 'r4mobilsevm', 'r5mobilsevm', 's1mobilsevm', 's2mobilsevm', 's3mobilsevm', 's4mobilsevm', 's5mobilsevm', 'r1mobilseva', 'r2mobilseva', 'r3mobilseva', 'r4mobilseva', 'r5mobilseva', 's1mobilseva', 's2mobilseva', 's3mobilseva', 's4mobilseva', 's5mobilseva', 'r1uppermob', 'r2uppermob', 'r3uppermob', 'r4uppermob', 'r5uppermob', 's1uppermob', 's2uppermob', 's3uppermob', 's4uppermob', 's5uppermob', 'r1uppermobm', 'r2uppermobm', 'r3uppermobm', 'r4uppermobm', 'r5uppermobm', 's1uppermobm', 's2uppermobm', 's3uppermobm', 's4uppermobm', 's5uppermobm', 'r1uppermoba', 'r2uppermoba', 'r3uppermoba', 'r4uppermoba', 'r5uppermoba', 's1uppermoba', 's2uppermoba', 's3uppermoba', 's4uppermoba', 's5uppermoba', 'r1lowermob', 'r2lowermob', 'r3lowermob', 'r4lowermob', 'r5lowermob', 's1lowermob', 's2lowermob', 's3lowermob', 's4lowermob', 's5lowermob', 'r1lowermobm', 'r2lowermobm', 'r3lowermobm', 'r4lowermobm', 'r5lowermobm', 's1lowermobm', 's2lowermobm', 's3lowermobm', 's4lowermobm', 's5lowermobm', 'r1lowermoba', 'r2lowermoba', 'r3lowermoba', 'r4lowermoba', 'r5lowermoba', 's1lowermoba', 's2lowermoba', 's3lowermoba', 's4lowermoba', 's5lowermoba', 'r1nagi10', 'r2nagi10', 'r3nagi10', 'r4nagi10', 'r5nagi10', 's1nagi10', 's2nagi10', 's3nagi10', 's4nagi10', 's5nagi10', 'r1nagi10m', 'r2nagi10m', 'r3nagi10m', 'r4nagi10m', 'r5nagi10m', 's1nagi10m', 's2nagi10m', 's3nagi10m', 's4nagi10m', 's5nagi10m', 'r1nagi10a', 'r2nagi10a', 'r3nagi10a', 'r4nagi10a', 'r5nagi10a', 's1nagi10a', 's2nagi10a', 's3nagi10a', 's4nagi10a', 's5nagi10a', 'r1nagi8', 'r2nagi8', 'r3nagi8', 'r4nagi8', 'r5nagi8', 's1nagi8', 's2nagi8', 's3nagi8', 's4nagi8', 's5nagi8', 'r1nagi8m', 'r2nagi8m', 'r3nagi8m', 'r4nagi8m', 'r5nagi8m', 's1nagi8m', 's2nagi8m', 's3nagi8m', 's4nagi8m', 's5nagi8m', 'r1nagi8a', 'r2nagi8a', 'r3nagi8a', 'r4nagi8a', 'r5nagi8a', 's1nagi8a', 's2nagi8a', 's3nagi8a', 's4nagi8a', 's5nagi8a']
# Doctor Diagnosed Health Problems: Ever Have Condition
Health11 = ['r1hibpe', 'r2hibpe', 'r3hibpe', 'r4hibpe', 'r5hibpe', 's1hibpe', 's2hibpe', 's3hibpe', 's4hibpe', 's5hibpe', 'r1diabe', 'r2diabe', 'r3diabe', 'r4diabe', 'r5diabe', 's1diabe', 's2diabe', 's3diabe', 's4diabe', 's5diabe', 'r1cancre', 'r2cancre', 'r3cancre', 'r4cancre', 'r5cancre', 's1cancre', 's2cancre', 's3cancre', 's4cancre', 's5cancre', 'r1respe', 'r2respe', 'r3respe', 'r4respe', 'r5respe', 's1respe', 's2respe', 's3respe', 's4respe', 's5respe', 'r1hrtatte', 'r2hrtatte', 'r3hrtatte', 'r4hrtatte', 'r5hrtatte', 's1hrtatte', 's2hrtatte', 's3hrtatte', 's4hrtatte', 's5hrtatte', 'r4hearte', 'r5hearte', 's4hearte', 's5hearte', 'r1stroke', 'r2stroke', 'r3stroke', 'r4stroke', 'r5stroke', 's1stroke', 's2stroke', 's3stroke', 's4stroke', 's5stroke', 'r1arthre', 'r2arthre', 'r3arthre', 'r4arthre', 'r5arthre', 's1arthre', 's2arthre', 's3arthre', 's4arthre', 's5arthre']
# Doctor Diagnosed Diseases: Whether Receives Treatment or Medication for Disease
Health12 = ['r1rxhibp', 'r2rxhibp', 'r3rxhibp', 'r4rxhibp', 'r5rxhibp', 's1rxhibp', 's2rxhibp', 's3rxhibp', 's4rxhibp', 's5rxhibp', 'r1rxdiabo', 'r2rxdiabo', 'r3rxdiabo', 'r4rxdiabo', 'r5rxdiabo', 's1rxdiabo', 's2rxdiabo', 's3rxdiabo', 's4rxdiabo', 's5rxdiabo', 'r1rxdiabi', 'r2rxdiabi', 'r3rxdiabi', 'r4rxdiabi', 'r5rxdiabi', 's1rxdiabi', 's2rxdiabi', 's3rxdiabi', 's4rxdiabi', 's5rxdiabi', 'r1rxdiab', 'r2rxdiab', 'r3rxdiab', 'r4rxdiab', 'r5rxdiab', 's1rxdiab', 's2rxdiab', 's3rxdiab', 's4rxdiab', 's5rxdiab', 'r1cncrchem', 'r2cncrchem', 'r3cncrchem', 'r4cncrchem', 'r5cncrchem', 's1cncrchem', 's2cncrchem', 's3cncrchem', 's4cncrchem', 's5cncrchem', 'r1cncrsurg', 'r2cncrsurg', 'r3cncrsurg', 'r4cncrsurg', 'r5cncrsurg', 's1cncrsurg', 's2cncrsurg', 's3cncrsurg', 's4cncrsurg', 's5cncrsurg', 'r1cncrradn', 'r2cncrradn', 'r3cncrradn', 'r4cncrradn', 'r5cncrradn', 's1cncrradn', 's2cncrradn', 's3cncrradn', 's4cncrradn', 's5cncrradn', 'r1cncrmeds', 'r2cncrmeds', 'r3cncrmeds', 'r4cncrmeds', 'r5cncrmeds', 's1cncrmeds', 's2cncrmeds', 's3cncrmeds', 's4cncrmeds', 's5cncrmeds', 'r1cncrothr', 'r2cncrothr', 'r3cncrothr', 'r4cncrothr', 'r5cncrothr', 's1cncrothr', 's2cncrothr', 's3cncrothr', 's4cncrothr', 's5cncrothr', 'r1rxresp', 'r2rxresp', 'r3rxresp', 'r4rxresp', 'r5rxresp', 's1rxresp', 's2rxresp', 's3rxresp', 's4rxresp', 's5rxresp', 'r1rxhrtat', 'r2rxhrtat', 'r3rxhrtat', 'r4rxhrtat', 'r5rxhrtat', 's1rxhrtat', 's2rxhrtat', 's3rxhrtat', 's4rxhrtat', 's5rxhrtat', 'r1rxstrok', 'r2rxstrok', 'r3rxstrok', 'r4rxstrok', 'r5rxstrok', 's1rxstrok', 's2rxstrok', 's3rxstrok', 's4rxstrok', 's5rxstrok', 'r1rxarthr', 'r2rxarthr', 'r3rxarthr', 'r4rxarthr', 'r5rxarthr', 's1rxarthr', 's2rxarthr', 's3rxarthr', 's4rxarthr', 's5rxarthr']
# Doctor Diagnosed Diseases: Whether Disease Limits Activity
Health13 = ['r1resplmt', 'r2resplmt', 'r3resplmt', 'r4resplmt', 'r5resplmt', 's1resplmt', 's2resplmt', 's3resplmt', 's4resplmt', 's5resplmt', 'r1hrtatlmt', 'r2hrtatlmt', 'r3hrtatlmt', 'r4hrtatlmt', 'r5hrtatlmt', 's1hrtatlmt', 's2hrtatlmt', 's3hrtatlmt', 's4hrtatlmt', 's5hrtatlmt', 'r1stroklmt', 'r2stroklmt', 'r3stroklmt', 'r4stroklmt', 'r5stroklmt', 's1stroklmt', 's2stroklmt', 's3stroklmt', 's4stroklmt', 's5stroklmt', 'r1arthlmt', 'r2arthlmt', 'r3arthlmt', 'r4arthlmt', 'r5arthlmt', 's1arthlmt', 's2arthlmt', 's3arthlmt', 's4arthlmt', 's5arthlmt']
# Doctor Diagnosed Diseases: Age of Diagnosis
Health14 = ['r1reccancr', 'r2reccancr', 'r3reccancr', 'r4reccancr', 'r5reccancr', 's1reccancr', 's2reccancr', 's3reccancr', 's4reccancr', 's5reccancr', 'r1rechrtatt', 'r2rechrtatt', 'r3rechrtatt', 'r4rechrtatt', 'r5rechrtatt', 's1rechrtatt', 's2rechrtatt', 's3rechrtatt', 's4rechrtatt', 's5rechrtatt', 'r1recstrok', 'r2recstrok', 'r3recstrok', 'r4recstrok', 'r5recstrok', 's1recstrok', 's2recstrok', 's3recstrok', 's4recstrok', 's5recstrok']
# Vision
Health15 = ['r1sight', 'r2sight', 'r3sight', 'r4sight', 'r5sight', 's1sight', 's2sight', 's3sight', 's4sight', 's5sight', 'r1glasses', 'r2glasses', 'r3glasses', 'r4glasses', 'r5glasses', 's1glasses', 's2glasses', 's3glasses', 's4glasses', 's5glasses']
# Hearing
Health16 = ['r1hearing', 'r2hearing', 'r3hearing', 'r4hearing', 'r5hearing', 's1hearing', 's2hearing', 's3hearing', 's4hearing', 's5hearing', 'r1hearaid', 'r2hearaid', 'r3hearaid', 'r4hearaid', 'r5hearaid', 's1hearaid', 's2hearaid', 's3hearaid', 's4hearaid', 's5hearaid']
# Falls
Health17 = ['r1fall', 'r2fall', 'r3fall', 'r4fall', 'r5fall', 's1fall', 's2fall', 's3fall', 's4fall', 's5fall', 'r1fallnum', 'r2fallnum', 'r3fallnum', 'r4fallnum', 'r5fallnum', 's1fallnum', 's2fallnum', 's3fallnum', 's4fallnum', 's5fallnum', 'r1fallinj', 'r2fallinj', 'r3fallinj', 'r4fallinj', 'r5fallinj', 's1fallinj', 's2fallinj', 's3fallinj', 's4fallinj', 's5fallinj', 'r1hip50e', 'r2hip50e', 'r3hip50e', 'r4hip50e', 's1hip50e', 's2hip50e', 's3hip50e', 's4hip50e', 'r3hip_m', 'r4hip_m', 'r5hip_m', 's3hip_m', 's4hip_m', 's5hip_m', 'r5hip', 's5hip']
# Urinary Incontinence
Health18 = ['r1urina2y', 'r2urina2y', 's1urina2y', 's2urina2y', 'r3urinurg2y', 'r4urinurg2y', 'r5urinurg2y', 's3urinurg2y', 's4urinurg2y', 's5urinurg2y', 'r3urincgh2y', 'r4urincgh2y', 'r5urincgh2y', 's3urincgh2y', 's4urincgh2y', 's5urincgh2y']
# Persistent Health Problems
Health19 = ['r1swell', 'r2swell', 'r3swell', 'r4swell', 'r5swell', 's1swell', 's2swell', 's3swell', 's4swell', 's5swell', 'r1breath_m', 'r2breath_m', 'r3breath_m', 'r4breath_m', 'r5breath_m', 's1breath_m', 's2breath_m', 's3breath_m', 's4breath_m', 's5breath_m', 'r1wheeze', 'r2wheeze', 's1wheeze', 's2wheeze', 'r1fatigue', 'r2fatigue', 'r3fatigue', 'r4fatigue', 'r5fatigue', 's1fatigue', 's2fatigue', 's3fatigue', 's4fatigue', 's5fatigue']
# Sleep
Health20 = ['r4fallslp', 'r5fallslp', 's4fallslp', 's5fallslp', 'r4wakent', 'r5wakent', 's4wakent', 's5wakent', 'r4wakeup', 'r5wakeup', 's4wakeup', 's5wakeup', 'r3rested', 'r4rested', 'r5rested', 's3rested', 's4rested', 's5rested']
# Pain
Health21 = ['r1painfr', 'r2painfr', 'r3painfr', 'r4painfr', 'r5painfr', 's1painfr', 's2painfr', 's3painfr', 's4painfr', 's5painfr', 'r1painlv', 'r2painlv', 'r3painlv', 'r4painlv', 'r5painlv', 's1painlv', 's2painlv', 's3painlv', 's4painlv', 's5painlv', 'r1paina', 'r2paina', 'r3paina', 'r4paina', 'r5paina', 's1paina', 's2paina', 's3paina', 's4paina', 's5paina']
# Menopause
Health22 = ['r4hystere', 'r5hystere', 's4hystere', 's5hystere', 'r4lstmnspd', 'r5lstmnspd', 's4lstmnspd', 's5lstmnspd', 'r4flstmnspd', 'r5flstmnspd', 's4flstmnspd', 's5flstmnspd']
# BMI
Health23 = ['r1bmi', 'r2bmi', 'r3bmi', 'r4bmi', 'r5bmi', 's1bmi', 's2bmi', 's3bmi', 's4bmi', 's5bmi', 'r1weight', 'r2weight', 'r3weight', 'r4weight', 'r5weight', 's1weight', 's2weight', 's3weight', 's4weight', 's5weight', 'r1height', 'r2height', 'r3height', 'r4height', 'r5height', 's1height', 's2height', 's3height', 's4height', 's5height']
# Health Behaviors: Physical Activity or Exercise
Health24 = ['r1vigact', 'r2vigact', 'r3vigact', 'r4vigact', 'r5vigact', 's1vigact', 's2vigact', 's3vigact', 's4vigact', 's5vigact']
# Health Behaviors: Drinking
Health25 = ['r1drink', 'r2drink', 'r3drink', 'r4drink', 'r5drink', 's1drink', 's2drink', 's3drink', 's4drink', 's5drink', 'r1drinkd', 'r2drinkd', 'r3drinkd', 'r4drinkd', 'r5drinkd', 's1drinkd', 's2drinkd', 's3drinkd', 's4drinkd', 's5drinkd', 'r1drinkn', 'r2drinkn', 'r3drinkn', 'r4drinkn', 'r5drinkn', 's1drinkn', 's2drinkn', 's3drinkn', 's4drinkn', 's5drinkn', 'r1drinkb', 'r2drinkb', 'r3drinkb', 'r4drinkb', 'r5drinkb', 's1drinkb', 's2drinkb', 's3drinkb', 's4drinkb', 's5drinkb', 'r1binged', 'r2binged', 'r3binged', 'r4binged', 'r5binged', 's1binged', 's2binged', 's3binged', 's4binged', 's5binged', 'r1drinkcut', 'r2drinkcut', 'r3drinkcut', 'r4drinkcut', 's1drinkcut', 's2drinkcut', 's3drinkcut', 's4drinkcut', 'r1drinkcr', 'r2drinkcr', 'r3drinkcr', 'r4drinkcr', 's1drinkcr', 's2drinkcr', 's3drinkcr', 's4drinkcr', 'r1drinkbd', 'r2drinkbd', 'r3drinkbd', 'r4drinkbd', 's1drinkbd', 's2drinkbd', 's3drinkbd', 's4drinkbd', 'r1drinknr', 'r2drinknr', 'r3drinknr', 'r4drinknr', 's1drinknr', 's2drinknr', 's3drinknr', 's4drinknr', 'r1cage', 'r2cage', 'r3cage', 'r4cage', 's1cage', 's2cage', 's3cage', 's4cage', 'r1cagem', 'r2cagem', 'r3cagem', 'r4cagem', 's1cagem', 's2cagem', 's3cagem', 's4cagem']
# Health Behaviors: Smoking (Cigarettes)
Health26 = ['r1smokev', 'r2smokev', 'r3smokev', 'r4smokev', 'r5smokev', 's1smokev', 's2smokev', 's3smokev', 's4smokev', 's5smokev', 'r1smoken', 'r2smoken', 'r3smoken', 'r4smoken', 'r5smoken', 's1smoken', 's2smoken', 's3smoken', 's4smoken', 's5smoken', 'r1smokef', 'r2smokef', 'r3smokef', 'r4smokef', 'r5smokef', 's1smokef', 's2smokef', 's3smokef', 's4smokef', 's5smokef', 'r1strtsmok', 'r2strtsmok', 'r3strtsmok', 'r4strtsmok', 'r5strtsmok', 's1strtsmok', 's2strtsmok', 's3strtsmok', 's4strtsmok', 's5strtsmok', 'r1quitsmok', 'r2quitsmok', 'r3quitsmok', 'r4quitsmok', 'r5quitsmok', 's1quitsmok', 's2quitsmok', 's3quitsmok', 's4quitsmok', 's5quitsmok']
# Health Behaviors: Preventive Care
Health27 = ['r1cholst', 'r2cholst', 'r3cholst', 'r4cholst', 'r5cholst', 's1cholst', 's2cholst', 's3cholst', 's4cholst', 's5cholst', 'r3flusht', 'r4flusht', 'r5flusht', 's3flusht', 's4flusht', 's5flusht', 'r1breast', 'r2breast', 'r3breast', 'r4breast', 'r5breast', 's1breast', 's2breast', 's3breast', 's4breast', 's5breast', 'r1mammog', 'r2mammog', 'r3mammog', 'r4mammog', 'r5mammog', 's1mammog', 's2mammog', 's3mammog', 's4mammog', 's5mammog', 'r1papsm', 'r2papsm', 'r3papsm', 'r4papsm', 'r5papsm', 's1papsm', 's2papsm', 's3papsm', 's4papsm', 's5papsm', 'r1prost', 'r2prost', 'r3prost', 'r4prost', 'r5prost', 's1prost', 's2prost', 's3prost', 's4prost', 's5prost']

# SECTION C: HEALTH CARE UTILIZATION AND INSURANCE (236 features)
# Medical Care Utilization: Hospital
HCare1 =['r1hosp1y', 'r2hosp1y', 'r3hosp1y', 'r4hosp1y', 'r5hosp1y', 's1hosp1y', 's2hosp1y', 's3hosp1y', 's4hosp1y', 's5hosp1y', 'r1hspnit1y', 'r2hspnit1y', 'r3hspnit1y', 'r4hspnit1y', 'r5hspnit1y', 's1hspnit1y', 's2hspnit1y', 's3hspnit1y', 's4hspnit1y', 's5hspnit1y']
# Medical Care Utilization: Doctor
HCare2 = ['r1doctor1y', 'r2doctor1y', 'r3doctor1y', 'r4doctor1y', 'r5doctor1y', 's1doctor1y', 's2doctor1y', 's3doctor1y', 's4doctor1y', 's5doctor1y', 'r1doctim1y', 'r2doctim1y', 'r3doctim1y', 'r4doctim1y', 'r5doctim1y', 's1doctim1y', 's2doctim1y', 's3doctim1y', 's4doctim1y', 's5doctim1y']
# Medical Care Utilization: Other Medical Care Utilization
HCare3 = ['r1outpt1y', 'r2outpt1y', 'r3outpt1y', 'r4outpt1y', 'r5outpt1y', 's1outpt1y', 's2outpt1y', 's3outpt1y', 's4outpt1y', 's5outpt1y', 'r1dentst1y', 'r2dentst1y', 'r3dentst1y', 'r4dentst1y', 'r5dentst1y', 's1dentst1y', 's2dentst1y', 's3dentst1y', 's4dentst1y', 's5dentst1y', 'r1dentim1y', 'r2dentim1y', 'r3dentim1y', 'r4dentim1y', 'r5dentim1y', 's1dentim1y', 's2dentim1y', 's3dentim1y', 's4dentim1y', 's5dentim1y']
# Medical Expenditures: Out of Pocket and Total
HCare4 = ['r1oophos1y', 'r2oophos1y', 'r3oophos1y', 'r4oophos1y', 'r5oophos1y', 's1oophos1y', 's2oophos1y', 's3oophos1y', 's4oophos1y', 's5oophos1y', 'r1oophosf1y', 'r2oophosf1y', 'r3oophosf1y', 'r4oophosf1y', 'r5oophosf1y', 's1oophosf1y', 's2oophosf1y', 's3oophosf1y', 's4oophosf1y', 's5oophosf1y', 'r1oopfhho1y', 'r2oopfhho1y', 'r3oopfhho1y', 'r4oopfhho1y', 's1oopfhho1y', 's2oopfhho1y', 's3oopfhho1y', 's4oopfhho1y', 'r1oopfhhof1y', 'r2oopfhhof1y', 'r3oopfhhof1y', 'r4oopfhhof1y', 's1oopfhhof1y', 's2oopfhhof1y', 's3oopfhhof1y', 's4oopfhhof1y', 'r1oopden1y', 'r2oopden1y', 'r3oopden1y', 'r4oopden1y', 'r5oopden1y', 's1oopden1y', 's2oopden1y', 's3oopden1y', 's4oopden1y', 's5oopden1y', 'r1oopdenf1y', 'r2oopdenf1y', 'r3oopdenf1y', 'r4oopdenf1y', 'r5oopdenf1y', 's1oopdenf1y', 's2oopdenf1y', 's3oopdenf1y', 's4oopdenf1y', 's5oopdenf1y', 'r1ooposrg1y', 'r2ooposrg1y', 'r3ooposrg1y', 'r4ooposrg1y', 'r5ooposrg1y', 's1ooposrg1y', 's2ooposrg1y', 's3ooposrg1y', 's4ooposrg1y', 's5ooposrg1y', 'r1ooposrgf1y', 'r2ooposrgf1y', 'r3ooposrgf1y', 'r4ooposrgf1y', 'r5ooposrgf1y', 's1ooposrgf1y', 's2ooposrgf1y', 's3ooposrgf1y', 's4ooposrgf1y', 's5ooposrgf1y', 'r1oopdoc1y', 'r2oopdoc1y', 'r3oopdoc1y', 'r4oopdoc1y', 'r5oopdoc1y', 's1oopdoc1y', 's2oopdoc1y', 's3oopdoc1y', 's4oopdoc1y', 's5oopdoc1y', 'r1oopdocf1y', 'r2oopdocf1y', 'r3oopdocf1y', 'r4oopdocf1y', 'r5oopdocf1y', 's1oopdocf1y', 's2oopdocf1y', 's3oopdocf1y', 's4oopdocf1y', 's5oopdocf1y', 'r1oopmd1y', 'r2oopmd1y', 'r3oopmd1y', 'r4oopmd1y', 'r5oopmd1y', 's1oopmd1y', 's2oopmd1y', 's3oopmd1y', 's4oopmd1y', 's5oopmd1y', 'r1oopmdf1y', 'r2oopmdf1y', 'r3oopmdf1y', 'r4oopmdf1y', 'r5oopmdf1y', 's1oopmdf1y', 's2oopmdf1y', 's3oopmdf1y', 's4oopmdf1y', 's5oopmdf1y']
# Covered by Federal Government Health Insurance Program
HCare5 = ['r1higov', 'r2higov', 'r3higov', 'r4higov', 'r5higov', 's1higov', 's2higov', 's3higov', 's4higov', 's5higov']
# Covered by Private Health Insurance
HCare6 = ['r1hipriv', 'r2hipriv', 'r3hipriv', 'r4hipriv', 'r5hipriv', 's1hipriv', 's2hipriv', 's3hipriv', 's4hipriv', 's5hipriv']
# Covered by Health Insurance from a Current or Previous Employer
HCare7 = ['r1covr_m', 'r2covr_m', 'r3covr_m', 'r4covr_m', 'r5covr_m', 's1covr_m', 's2covr_m', 's3covr_m', 's4covr_m', 's5covr_m', 'r1covs_m', 'r2covs_m', 'r3covs_m', 'r4covs_m', 'r5covs_m', 's1covs_m', 's2covs_m', 's3covs_m', 's4covs_m', 's5covs_m']
# Number of Health Insurance Plans
HCare8 = ['r1henum', 'r2henum', 'r3henum', 'r4henum', 'r5henum', 's1henum', 's2henum', 's3henum', 's4henum', 's5henum']

# SECTION D: COGNITION (706 features)
# Cognition Testing Conditions
Cognit1 =['r1novisual', 'r2novisual', 'r3novisual', 'r4novisual', 'r5novisual', 's1novisual', 's2novisual', 's3novisual', 's4novisual', 's5novisual', 'r1nopencil', 'r2nopencil', 'r3nopencil', 'r4nopencil', 'r5nopencil', 's1nopencil', 's2nopencil', 's3nopencil', 's4nopencil', 's5nopencil']
# Self-Reported Memory
Cognit2 =['r3slfmem', 'r4slfmem', 'r5slfmem', 's3slfmem', 's4slfmem', 's5slfmem', 'r3pstmem', 'r4pstmem', 'r5pstmem', 's3pstmem', 's4pstmem', 's5pstmem']
# Immediate Word Recall
Cognit3 =['r1imrc8', 'r2imrc8', 'r3imrc8', 'r4imrc8', 'r5imrc8', 's1imrc8', 's2imrc8', 's3imrc8', 's4imrc8', 's5imrc8', 'r1fimrc8', 'r2fimrc8', 'r3fimrc8', 'r4fimrc8', 'r5fimrc8', 's1fimrc8', 's2fimrc8', 's3fimrc8', 's4fimrc8', 's5fimrc8']
# Delayed Word Recall
Cognit4 =['r1dlrc8', 'r2dlrc8', 'r3dlrc8', 'r4dlrc8', 'r5dlrc8', 's1dlrc8', 's2dlrc8', 's3dlrc8', 's4dlrc8', 's5dlrc8', 'r1fdlrc8', 'r2fdlrc8', 'r3fdlrc8', 'r4fdlrc8', 'r5fdlrc8', 's1fdlrc8', 's2fdlrc8', 's3fdlrc8', 's4fdlrc8', 's5fdlrc8']
# Summary Scores
Cognit5 =['r1tr16', 'r2tr16', 'r3tr16', 'r4tr16', 'r5tr16', 's1tr16', 's2tr16', 's3tr16', 's4tr16', 's5tr16', 'r1ftr16', 'r2ftr16', 'r3ftr16', 'r4ftr16', 'r5ftr16', 's1ftr16', 's2ftr16', 's3ftr16', 's4ftr16', 's5ftr16']
# Picture Drawing
Cognit6 =['r1idraw2', 'r2idraw2', 's1idraw2', 's2idraw2', 'r1fidraw2', 'r2fidraw2', 's1fidraw2', 's2fidraw2', 'r3idraw1', 'r4idraw1', 'r5idraw1', 's3idraw1', 's4idraw1', 's5idraw1', 'r3fidraw1', 'r4fidraw1', 'r5fidraw1', 's3fidraw1', 's4fidraw1', 's5fidraw1', 'r1ddraw2', 'r2ddraw2', 's1ddraw2', 's2ddraw2', 'r1fddraw2', 'r2fddraw2', 's1fddraw2', 's2fddraw2', 'r3ddraw1', 'r4ddraw1', 'r5ddraw1', 's3ddraw1', 's4ddraw1', 's5ddraw1', 'r3fddraw1', 'r4fddraw1', 'r5fddraw1', 's3fddraw1', 's4fddraw1', 's5fddraw1']
# Verbal Fluency
Cognit7 =['r3verbf', 'r4verbf', 'r5verbf', 's3verbf', 's4verbf', 's5verbf', 'r3fverbf', 'r4fverbf', 'r5fverbf', 's3fverbf', 's4fverbf', 's5fverbf']
# Visual Scanning
Cognit8 =['r1vscan', 'r2vscan', 'r3vscan', 'r4vscan', 'r5vscan', 's1vscan', 's2vscan', 's3vscan', 's4vscan', 's5vscan', 'r1fvscan', 'r2fvscan', 'r3fvscan', 'r4fvscan', 'r5fvscan', 's1fvscan', 's2fvscan', 's3fvscan', 's4fvscan', 's5fvscan']
# Backwards Counting From 20
Cognit9 =['r3bwc20', 'r4bwc20', 's3bwc20', 's4bwc20', 'r3bwc20_m', 'r4bwc20_m', 's3bwc20_m', 's4bwc20_m', 'r3fbwc20_m', 'r4fbwc20_m', 's3fbwc20_m', 's4fbwc20_m']
# Date Naming/Orientation
Cognit10 =['r2dy', 'r3dy', 'r4dy', 'r5dy', 's2dy', 's3dy', 's4dy', 's5dy', 'r2fdy', 'r3fdy', 'r4fdy', 'r5fdy', 's2fdy', 's3fdy', 's4fdy', 's5fdy', 'r2mo', 'r3mo', 'r4mo', 'r5mo', 's2mo', 's3mo', 's4mo', 's5mo', 'r2fmo', 'r3fmo', 'r4fmo', 'r5fmo', 's2fmo', 's3fmo', 's4fmo', 's5fmo', 'r2yr', 'r3yr', 'r4yr', 'r5yr', 's2yr', 's3yr', 's4yr', 's5yr', 'r2fyr', 'r3fyr', 'r4fyr', 'r5fyr', 's2fyr', 's3fyr', 's4fyr', 's5fyr', 'r2orient_m', 'r3orient_m', 'r4orient_m', 'r5orient_m', 's2orient_m', 's3orient_m', 's4orient_m', 's5orient_m', 'r2forient_m', 'r3forient_m', 'r4forient_m', 'r5forient_m', 's2forient_m', 's3forient_m', 's4forient_m', 's5forient_m']
# Serial 7’s
Cognit11 =['r4ser7', 'r5ser7', 's4ser7', 's5ser7', 'r4fser7', 'r5fser7', 's4fser7', 's5fser7']
# Proxy Cognition: JORM IQCODE
Cognit12 =['r1ciqscore1', 'r2ciqscore1', 'r3ciqscore1', 'r4ciqscore1', 'r5ciqscore1', 's1ciqscore1', 's2ciqscore1', 's3ciqscore1', 's4ciqscore1', 's5ciqscore1', 'r1fciqscore1', 'r2fciqscore1', 'r3fciqscore1', 'r4fciqscore1', 'r5fciqscore1', 's1fciqscore1', 's2fciqscore1', 's3fciqscore1', 's4fciqscore1', 's5fciqscore1', 'r1ciqscore2', 'r2ciqscore2', 'r3ciqscore2', 'r4ciqscore2', 'r5ciqscore2', 's1ciqscore2', 's2ciqscore2', 's3ciqscore2', 's4ciqscore2', 's5ciqscore2', 'r1fciqscore2', 'r2fciqscore2', 'r3fciqscore2', 'r4fciqscore2', 'r5fciqscore2', 's1fciqscore2', 's2fciqscore2', 's3fciqscore2', 's4fciqscore2', 's5fciqscore2', 'r1ciqscore3', 'r2ciqscore3', 'r3ciqscore3', 'r4ciqscore3', 'r5ciqscore3', 's1ciqscore3', 's2ciqscore3', 's3ciqscore3', 's4ciqscore3', 's5ciqscore3', 'r1fciqscore3', 'r2fciqscore3', 'r3fciqscore3', 'r4fciqscore3', 'r5fciqscore3', 's1fciqscore3', 's2fciqscore3', 's3fciqscore3', 's4fciqscore3', 's5fciqscore3', 'r1ciqscore4', 'r2ciqscore4', 'r3ciqscore4', 'r4ciqscore4', 'r5ciqscore4', 's1ciqscore4', 's2ciqscore4', 's3ciqscore4', 's4ciqscore4', 's5ciqscore4', 'r1fciqscore4', 'r2fciqscore4', 'r3fciqscore4', 'r4fciqscore4', 'r5fciqscore4', 's1fciqscore4', 's2fciqscore4', 's3fciqscore4', 's4fciqscore4', 's5fciqscore4', 'r1ciqscore5', 'r2ciqscore5', 'r3ciqscore5', 'r4ciqscore5', 'r5ciqscore5', 's1ciqscore5', 's2ciqscore5', 's3ciqscore5', 's4ciqscore5', 's5ciqscore5', 'r1fciqscore5', 'r2fciqscore5', 'r3fciqscore5', 'r4fciqscore5', 'r5fciqscore5', 's1fciqscore5', 's2fciqscore5', 's3fciqscore5', 's4fciqscore5', 's5fciqscore5', 'r1ciqscore6', 'r2ciqscore6', 'r3ciqscore6', 'r4ciqscore6', 'r5ciqscore6', 's1ciqscore6', 's2ciqscore6', 's3ciqscore6', 's4ciqscore6', 's5ciqscore6', 'r1fciqscore6', 'r2fciqscore6', 'r3fciqscore6', 'r4fciqscore6', 'r5fciqscore6', 's1fciqscore6', 's2fciqscore6', 's3fciqscore6', 's4fciqscore6', 's5fciqscore6', 'r1ciqscore7', 'r2ciqscore7', 'r3ciqscore7', 'r4ciqscore7', 'r5ciqscore7', 's1ciqscore7', 's2ciqscore7', 's3ciqscore7', 's4ciqscore7', 's5ciqscore7', 'r1fciqscore7', 'r2fciqscore7', 'r3fciqscore7', 'r4fciqscore7', 'r5fciqscore7', 's1fciqscore7', 's2fciqscore7', 's3fciqscore7', 's4fciqscore7', 's5fciqscore7', 'r1ciqscore8', 'r2ciqscore8', 'r3ciqscore8', 'r4ciqscore8', 'r5ciqscore8', 's1ciqscore8', 's2ciqscore8', 's3ciqscore8', 's4ciqscore8', 's5ciqscore8', 'r1fciqscore8', 'r2fciqscore8', 'r3fciqscore8', 'r4fciqscore8', 'r5fciqscore8', 's1fciqscore8', 's2fciqscore8', 's3fciqscore8', 's4fciqscore8', 's5fciqscore8', 'r1ciqscore9', 'r2ciqscore9', 'r3ciqscore9', 'r4ciqscore9', 'r5ciqscore9', 's1ciqscore9', 's2ciqscore9', 's3ciqscore9', 's4ciqscore9', 's5ciqscore9', 'r1fciqscore9', 'r2fciqscore9', 'r3fciqscore9', 'r4fciqscore9', 'r5fciqscore9', 's1fciqscore9', 's2fciqscore9', 's3fciqscore9', 's4fciqscore9', 's5fciqscore9', 'r1ciqscore10', 'r2ciqscore10', 'r3ciqscore10', 'r4ciqscore10', 'r5ciqscore10', 's1ciqscore10', 's2ciqscore10', 's3ciqscore10', 's4ciqscore10', 's5ciqscore10', 'r1fciqscore10', 'r2fciqscore10', 'r3fciqscore10', 'r4fciqscore10', 'r5fciqscore10', 's1fciqscore10', 's2fciqscore10', 's3fciqscore10', 's4fciqscore10', 's5fciqscore10', 'r1ciqscore11', 'r2ciqscore11', 'r3ciqscore11', 'r4ciqscore11', 'r5ciqscore11', 's1ciqscore11', 's2ciqscore11', 's3ciqscore11', 's4ciqscore11', 's5ciqscore11', 'r1fciqscore11', 'r2fciqscore11', 'r3fciqscore11', 'r4fciqscore11', 'r5fciqscore11', 's1fciqscore11', 's2fciqscore11', 's3fciqscore11', 's4fciqscore11', 's5fciqscore11', 'r1ciqscore12', 'r2ciqscore12', 'r3ciqscore12', 'r4ciqscore12', 'r5ciqscore12', 's1ciqscore12', 's2ciqscore12', 's3ciqscore12', 's4ciqscore12', 's5ciqscore12', 'r1fciqscore12', 'r2fciqscore12', 'r3fciqscore12', 'r4fciqscore12', 'r5fciqscore12', 's1fciqscore12', 's2fciqscore12', 's3fciqscore12', 's4fciqscore12', 's5fciqscore12', 'r1ciqscore13', 'r2ciqscore13', 'r3ciqscore13', 'r4ciqscore13', 'r5ciqscore13', 's1ciqscore13', 's2ciqscore13', 's3ciqscore13', 's4ciqscore13', 's5ciqscore13', 'r1fciqscore13', 'r2fciqscore13', 'r3fciqscore13', 'r4fciqscore13', 'r5fciqscore13', 's1fciqscore13', 's2fciqscore13', 's3fciqscore13', 's4fciqscore13', 's5fciqscore13', 'r1ciqscore14', 'r2ciqscore14', 'r3ciqscore14', 'r4ciqscore14', 'r5ciqscore14', 's1ciqscore14', 's2ciqscore14', 's3ciqscore14', 's4ciqscore14', 's5ciqscore14', 'r1fciqscore14', 'r2fciqscore14', 'r3fciqscore14', 'r4fciqscore14', 'r5fciqscore14', 's1fciqscore14', 's2fciqscore14', 's3fciqscore14', 's4fciqscore14', 's5fciqscore14', 'r1ciqscore15', 'r2ciqscore15', 'r3ciqscore15', 'r4ciqscore15', 'r5ciqscore15', 's1ciqscore15', 's2ciqscore15', 's3ciqscore15', 's4ciqscore15', 's5ciqscore15', 'r1fciqscore15', 'r2fciqscore15', 'r3fciqscore15', 'r4fciqscore15', 'r5fciqscore15', 's1fciqscore15', 's2fciqscore15', 's3fciqscore15', 's4fciqscore15', 's5fciqscore15', 'r1ciqscore16', 'r2ciqscore16', 'r3ciqscore16', 'r4ciqscore16', 'r5ciqscore16', 's1ciqscore16', 's2ciqscore16', 's3ciqscore16', 's4ciqscore16', 's5ciqscore16', 'r1fciqscore16', 'r2fciqscore16', 'r3fciqscore16', 'r4fciqscore16', 'r5fciqscore16', 's1fciqscore16', 's2fciqscore16', 's3fciqscore16', 's4fciqscore16', 's5fciqscore16', 'r1cjormscore', 'r2cjormscore', 'r3cjormscore', 'r4cjormscore', 'r5cjormscore', 's1cjormscore', 's2cjormscore', 's3cjormscore', 's4cjormscore', 's5cjormscore']
# Proxy Cognition: Ratings of Memory and Abilities
Cognit13 =['r1prmem', 'r2prmem', 'r3prmem', 'r4prmem', 'r5prmem', 's1prmem', 's2prmem', 's3prmem', 's4prmem', 's5prmem', 'r1prchmem', 'r2prchmem', 'r3prchmem', 'r4prchmem', 'r5prchmem', 's1prchmem', 's2prchmem', 's3prchmem', 's4prchmem', 's5prchmem', 'r1rjudg', 'r2rjudg', 'r3rjudg', 'r4rjudg', 'r5rjudg', 's1rjudg', 's2rjudg', 's3rjudg', 's4rjudg', 's5rjudg', 'r1rorgnz', 'r2rorgnz', 'r3rorgnz', 'r4rorgnz', 'r5rorgnz', 's1rorgnz', 's2rorgnz', 's3rorgnz', 's4rorgnz', 's5rorgnz']
# Proxy Cognition: Cognitive Impairment
Cognit14 =['r1lost', 'r2lost', 'r3lost', 'r4lost', 'r5lost', 's1lost', 's2lost', 's3lost', 's4lost', 's5lost', 'r1wander', 'r2wander', 'r3wander', 'r4wander', 'r5wander', 's1wander', 's2wander', 's3wander', 's4wander', 's5wander', 'r1alone', 'r2alone', 'r3alone', 'r4alone', 'r5alone', 's1alone', 's2alone', 's3alone', 's4alone', 's5alone', 'r1haluc', 'r2haluc', 'r3haluc', 'r4haluc', 'r5haluc', 's1haluc', 's2haluc', 's3haluc', 's4haluc', 's5haluc']
# Proxy Cognition: Problem Behaviors in Past Week
Cognit15 =['r1oangry', 'r2oangry', 'r3oangry', 'r4oangry', 's1oangry', 's2oangry', 's3oangry', 's4oangry', 'r1osleep', 'r2osleep', 'r3osleep', 'r4osleep', 's1osleep', 's2osleep', 's3osleep', 's4osleep', 'r1odngr', 'r2odngr', 'r3odngr', 'r4odngr', 's1odngr', 's2odngr', 's3odngr', 's4odngr', 'r1opace', 'r2opace', 'r3opace', 'r4opace', 's1opace', 's2opace', 's3opace', 's4opace', 'r1oplot', 'r2oplot', 'r3oplot', 'r4oplot', 's1oplot', 's2oplot', 's3oplot', 's4oplot', 'r1oalchl', 'r2oalchl', 'r3oalchl', 'r4oalchl', 's1oalchl', 's2oalchl', 's3oalchl', 's4oalchl']

# SECTION E: FINANCIAL AND HOUSING WEALTH (148 features)
# Inflation Multiplier
Financ1 =['c2000cpindex', 'c2001cpindex', 'c2002cpindex', 'c2003cpindex', 'c2011cpindex', 'c2012cpindex', 'c2013cpindex', 'c2014cpindex', 'c2015cpindex', 'c2016cpindex', 'c2017cpindex', 'c2018cpindex', 'c2019cpindex']
# Net Value of Real Estate (Not Primary Residence)
Financ2 =['h1arles', 'h2arles', 'h3arles', 'h4arles', 'h5arles', 'h1afrles', 'h2afrles', 'h3afrles', 'h4afrles', 'h5afrles']
# Net Value of Cars
Financ3 =['h1atran', 'h2atran', 'h3atran', 'h4atran', 'h5atran', 'h1aftran', 'h2aftran', 'h3aftran', 'h4aftran', 'h5aftran']
# Net Value of Businesses 
Financ4 =['h1absns', 'h2absns', 'h3absns', 'h4absns', 'h5absns', 'h1afbsns', 'h2afbsns', 'h3afbsns', 'h4afbsns', 'h5afbsns']
# Value of Stocks, Shares, and Bonds
Financ5 =['h1abdstk', 'h2abdstk', 'h3abdstk', 'h4abdstk', 'h5abdstk', 'h1afbdstk', 'h2afbdstk', 'h3afbdstk', 'h4afbdstk', 'h5afbdstk']
# Value of Checking, Savings Accounts
Financ6 =['h1achck', 'h2achck', 'h3achck', 'h4achck', 'h5achck', 'h1afchck', 'h2afchck', 'h3afchck', 'h4afchck', 'h5afchck']
# Value of Other Assets
Financ7 =['h1aothr', 'h2aothr', 'h3aothr', 'h4aothr', 'h5aothr', 'h1afothr', 'h2afothr', 'h3afothr', 'h4afothr', 'h5afothr']
# Value of Primary Residence
Financ8 =['h1ahous', 'h2ahous', 'h3ahous', 'h4ahous', 'h5ahous', 'h1afhous', 'h2afhous', 'h3afhous', 'h4afhous', 'h5afhous']
# Value of All Mortgages (Primary Residence)
Financ9 =['h1amort', 'h2amort', 'h3amort', 'h4amort', 'h5amort', 'h1afmort', 'h2afmort', 'h3afmort', 'h4afmort', 'h5afmort']
# Net Value of Primary Residence
Financ10 =['h1atoth', 'h2atoth', 'h3atoth', 'h4atoth', 'h5atoth', 'h1aftoth', 'h2aftoth', 'h3aftoth', 'h4aftoth', 'h5aftoth']
# Home ownership
Financ11 =['h1hownrnt', 'h2hownrnt', 'h3hownrnt', 'h4hownrnt', 'h5hownrnt']
# Value of Other Debt
Financ12 =['h1adebt', 'h2adebt', 'h3adebt', 'h4adebt', 'h5adebt', 'h1afdebt', 'h2afdebt', 'h3afdebt', 'h4afdebt', 'h5afdebt']
# Value of Loans Lent
Financ13 =['h1alend', 'h2alend', 'h3alend', 'h4alend', 'h5alend', 'h1aflend', 'h2aflend', 'h3aflend', 'h4aflend', 'h5aflend']
# Net Value of Non-Housing Financial Wealth (Excluding IRAs)
Financ14 =['h1atotf', 'h2atotf', 'h3atotf', 'h4atotf', 'h5atotf', 'h1aftotf', 'h2aftotf', 'h3aftotf', 'h4aftotf', 'h5aftotf']
# Total Wealth
Financ15 =['h1atotb', 'h2atotb', 'h3atotb', 'h4atotb', 'h5atotb', 'h1aftotb', 'h2aftotb', 'h3aftotb', 'h4aftotb', 'h5aftotb']

# SECTION F: INCOME (212 features)
# Individual Earnings
Incom1 = ['r1iearn', 'r2iearn', 'r3iearn', 'r4iearn', 'r5iearn', 's1iearn', 's2iearn', 's3iearn', 's4iearn', 's5iearn', 'r1ifearn', 'r2ifearn', 'r3ifearn', 'r4ifearn', 'r5ifearn', 's1ifearn', 's2ifearn', 's3ifearn', 's4ifearn', 's5ifearn']
# Household Capital Income
Incom2 = ['h1isemp', 'h2isemp', 'h3isemp', 'h4isemp', 'h5isemp', 'h1ifsemp', 'h2ifsemp', 'h3ifsemp', 'h4ifsemp', 'h5ifsemp', 'h1irent', 'h2irent', 'h3irent', 'h4irent', 'h5irent', 'h1ifrent', 'h2ifrent', 'h3ifrent', 'h4ifrent', 'h5ifrent', 'h1itrest', 'h2itrest', 'h3itrest', 'h4itrest', 'h5itrest', 'h1iftrest', 'h2iftrest', 'h3iftrest', 'h4iftrest', 'h5iftrest', 'h1icap', 'h2icap', 'h3icap', 'h4icap', 'h5icap', 'h1ifcap', 'h2ifcap', 'h3ifcap', 'h4ifcap', 'h5ifcap']
# Individual Income from Private Pension
Incom3 = ['r1ipena', 'r2ipena', 'r5ipena', 's1ipena', 's2ipena', 's5ipena', 'r1ifpena', 'r2ifpena', 'r5ifpena', 's1ifpena', 's2ifpena', 's5ifpena']
# Individual Public Pension Income
Incom4 = ['r1isret', 'r2isret', 'r5isret', 's1isret', 's2isret', 's5isret', 'r1ifsret', 'r2ifsret', 'r5ifsret', 's1ifsret', 's2ifsret', 's5ifsret', 'r1issdi', 'r2issdi', 'r5issdi', 's1issdi', 's2issdi', 's5issdi', 'r1ifssdi', 'r2ifssdi', 'r5ifssdi', 's1ifssdi', 's2ifssdi', 's5ifssdi', 'r1ipubo', 'r2ipubo', 'r5ipubo', 's1ipubo', 's2ipubo', 's5ipubo', 'r1ifpubo', 'r2ifpubo', 'r5ifpubo', 's1ifpubo', 's2ifpubo', 's5ifpubo', 'r1ipubpen', 'r2ipubpen', 'r5ipubpen', 's1ipubpen', 's2ipubpen', 's5ipubpen', 'r1ifpubpen', 'r2ifpubpen', 'r5ifpubpen', 's1ifpubpen', 's2ifpubpen', 's5ifpubpen']
# Individual Other Pensions Income
Incom5 = ['r1ipeno', 'r2ipeno', 'r5ipeno', 's1ipeno', 's2ipeno', 's5ipeno', 'r1ifpeno', 'r2ifpeno', 'r5ifpeno', 's1ifpeno', 's2ifpeno', 's5ifpeno']
# Individual Total Pensions Income
Incom6 = ['r1ipent', 'r2ipent', 'r3ipent', 'r4ipent', 'r5ipent', 's1ipent', 's2ipent', 's3ipent', 's4ipent', 's5ipent', 'r1ifpent', 'r2ifpent', 'r3ifpent', 'r4ifpent', 'r5ifpent', 's1ifpent', 's2ifpent', 's3ifpent', 's4ifpent', 's5ifpent']
# Individual Income from Other Government Transfers
Incom7 = ['r1igxfr', 'r2igxfr', 'r3igxfr', 'r4igxfr', 'r5igxfr', 's1igxfr', 's2igxfr', 's3igxfr', 's4igxfr', 's5igxfr', 'r1ifgxfr', 'r2ifgxfr', 'r3ifgxfr', 'r4ifgxfr', 'r5ifgxfr', 's1ifgxfr', 's2ifgxfr', 's3ifgxfr', 's4ifgxfr', 's5ifgxfr']
# All Other Income
Incom8 = ['r1iothr', 'r2iothr', 'r3iothr', 'r4iothr', 'r5iothr', 's1iothr', 's2iothr', 's3iothr', 's4iothr', 's5iothr', 'r1ifothr', 'r2ifothr', 'r3ifothr', 'r4ifothr', 'r5ifothr', 's1ifothr', 's2ifothr', 's3ifothr', 's4ifothr', 's5ifothr']
# Total Household Income (respondent & spouse)
Incom9 = ['h1itot', 'h2itot', 'h3itot', 'h4itot', 'h5itot', 'h1iftot', 'h2iftot', 'h3iftot', 'h4iftot', 'h5iftot']
# Total Household Consumption (full household)
Incom10 = ['h1ctot1m', 'h2ctot1m', 'h3ctot1m', 'h4ctot1m', 'h5ctot1m', 'h1cftot1m', 'h2cftot1m', 'h3cftot1m', 'h4cftot1m', 'h5cftot1m']

# SECTION G: FAMILY STRUCTURE (223 features)
# Number of People Living in Household
Family1=['h1hhres', 'h2hhres', 'h3hhres', 'h4hhres', 'h5hhres']
# Number of Living Children
Family2=['h1child', 'h2child', 'h3child', 'h4child', 'h5child', 'h1son', 'h2son', 'h3son', 'h4son', 'h5son', 'h1dau', 'h2dau', 'h3dau', 'h4dau', 'h5dau']
# Number of Deceased Children
Family3=['h1dchild', 'h2dchild', 'h3dchild', 'h4dchild', 'h5dchild']
# Number of Children Ever Born
Family4=['raevbrn', 's1evbrn', 's2evbrn', 's3evbrn', 's4evbrn', 's5evbrn']
# Number of Grandchildren
Family5=['h1grchild', 'h2grchild', 'h3grchild', 'h4grchild', 'h5grchild']
# Number of Living Siblings
Family6=['r1livsib', 'r2livsib', 'r3livsib', 'r4livsib', 'r5livsib', 's1livsib', 's2livsib', 's3livsib', 's4livsib', 's5livsib']
# Number of Deceased Siblings
Family7=['r1decsib', 'r2decsib', 'r3decsib', 'r4decsib', 'r5decsib', 's1decsib', 's2decsib', 's3decsib', 's4decsib', 's5decsib']
# Number of Living Parents
Family8=['r1livpar', 'r2livpar', 'r3livpar', 'r4livpar', 'r5livpar', 's1livpar', 's2livpar', 's3livpar', 's4livpar', 's5livpar']
# Parental Mortality
Family9=['r1momliv', 'r2momliv', 'r3momliv', 'r4momliv', 'r5momliv', 's1momliv', 's2momliv', 's3momliv', 's4momliv', 's5momliv', 'r1dadliv', 'r2dadliv', 'r3dadliv', 'r4dadliv', 'r5dadliv', 's1dadliv', 's2dadliv', 's3dadliv', 's4dadliv', 's5dadliv']
# Parents' Current Age or Age at Death
Family10=['r1momage', 'r2momage', 'r3momage', 'r4momage', 'r5momage', 's1momage', 's2momage', 's3momage', 's4momage', 's5momage', 'r1dadage', 'r2dadage', 'r3dadage', 'r4dadage', 'r5dadage', 's1dadage', 's2dadage', 's3dadage', 's4dadage', 's5dadage']
# Parents' Education
Family11=['rameduc_m', 's1meduc_m', 's2meduc_m', 's3meduc_m', 's4meduc_m', 's5meduc_m', 'rafeduc_m', 's1feduc_m', 's2feduc_m', 's3feduc_m', 's4feduc_m', 's5feduc_m']
# Any Child Co-Resides with Respondent
Family12=['h1coresd', 'h2coresd', 'h3coresd', 'h4coresd', 'h5coresd']
# Any Children Living in the Same City
Family13=['h1lvnear', 'h2lvnear', 'h3lvnear', 'h4lvnear', 'h5lvnear']
# Any Weekly Contact with Children
Family14=['h1kcnt', 'h2kcnt', 'h3kcnt', 'h4kcnt', 'h5kcnt']
# Frequent or Weekly Contact with Relatives and Friends
Family15=['r3rfcnt', 'r4rfcnt', 'r5rfcnt', 's3rfcnt', 's4rfcnt', 's5rfcnt', 'r3rfcntx_m', 'r4rfcntx_m', 'r5rfcntx_m', 's3rfcntx_m', 's4rfcntx_m', 's5rfcntx_m']
# Any Weekly Social Activities or Participate in Religious Groups
Family16=['r3socwk', 'r4socwk', 'r5socwk', 's3socwk', 's4socwk', 's5socwk', 'r3socact_m', 'r4socact_m', 'r5socact_m', 's3socact_m', 's4socact_m', 's5socact_m', 'r3relgwk', 'r4relgwk', 'r5relgwk', 's3relgwk', 's4relgwk', 's5relgwk', 'r1relgimp', 'r2relgimp', 'r3relgimp', 'r4relgimp', 'r5relgimp', 's1relgimp', 's2relgimp', 's3relgimp', 's4relgimp', 's5relgimp']
# Financial Transfer from Children
Family17=['h1fcany', 'h2fcany', 'h3fcany', 'h4fcany', 'h5fcany', 'h1fcamt', 'h2fcamt', 'h3fcamt', 'h4fcamt', 'h1fcflag', 'h2fcflag', 'h3fcflag', 'h4fcflag']
# Financial Transfer to Children
Family18=['h1tcany', 'h2tcany', 'h3tcany', 'h4tcany', 'h5tcany', 'h1tcamt', 'h2tcamt', 'h3tcamt', 'h4tcamt', 'h1tcflag', 'h2tcflag', 'h3tcflag', 'h4tcflag']
# Financial Transfer to Parents
Family19=['r1tpany', 'r2tpany', 'r3tpany', 'r4tpany', 'r5tpany', 's1tpany', 's2tpany', 's3tpany', 's4tpany', 's5tpany', 'r1tpamt', 'r2tpamt', 'r3tpamt', 'r4tpamt', 's1tpamt', 's2tpamt', 's3tpamt', 's4tpamt', 'r2tpflag', 'r3tpflag', 'r4tpflag', 's2tpflag', 's3tpflag', 's4tpflag']

# SECTION H: EMPLOYMENT HISTORY (110 features)
# Currently Working for Pay
Employ1=['r1work', 'r2work', 'r3work', 'r4work', 'r5work', 's1work', 's2work', 's3work', 's4work', 's5work']
# Whether Self-Employed
Employ2=['r1slfemp', 'r2slfemp', 'r3slfemp', 'r4slfemp', 'r5slfemp', 's1slfemp', 's2slfemp', 's3slfemp', 's4slfemp', 's5slfemp']
# Labor Force Status
Employ3=['r1lbrf_m', 'r2lbrf_m', 'r3lbrf_m', 'r4lbrf_m', 'r5lbrf_m', 's1lbrf_m', 's2lbrf_m', 's3lbrf_m', 's4lbrf_m', 's5lbrf_m']
# In the Labor Force
Employ4=['r2inlbrf', 'r3inlbrf', 'r4inlbrf', 'r5inlbrf', 's2inlbrf', 's3inlbrf', 's4inlbrf', 's5inlbrf']
# Unemployment Status
Employ5=['r1unemp', 'r2unemp', 'r3unemp', 'r4unemp', 'r5unemp', 's1unemp', 's2unemp', 's3unemp', 's4unemp', 's5unemp']
# Retired Employment Status
Employ6=['r2retemp', 'r3retemp', 'r4retemp', 'r5retemp', 's2retemp', 's3retemp', 's4retemp', 's5retemp']
# Hours at Main Job
Employ7=['r1jhoursd', 's1jhoursd', 'r2jhours', 'r3jhours', 'r4jhours', 'r5jhours', 's2jhours', 's3jhours', 's4jhours', 's5jhours']
# Main Activity Years of Tenure
Employ8=['r1jcten', 'r2jcten', 'r3jcten', 'r4jcten', 'r5jcten', 's1jcten', 's2jcten', 's3jcten', 's4jcten', 's5jcten']
# Job Allows Move to Less Demanding Work
Employ9=['r2jredhr', 'r3jredhr', 'r4jredhr', 'r5jredhr', 's2jredhr', 's3jredhr', 's4jredhr', 's5jredhr']
# Occupation Code for Job with Longest Reported Tenure
Employ10=['r1jlocc_m', 'r2jlocc_m', 'r3jlocc_m', 'r4jlocc_m', 'r5jlocc_m', 's1jlocc_m', 's2jlocc_m', 's3jlocc_m', 's4jlocc_m', 's5jlocc_m']
# Year Last Job Ended
Employ11=['r2jlasty', 'r3jlasty', 'r4jlasty', 'r5jlasty', 's2jlasty', 's3jlasty', 's4jlasty', 's5jlasty']
# Reason Job Ended
Employ12=['r2jrsleft', 'r3jrsleft', 'r4jrsleft', 'r5jrsleft', 's2jrsleft', 's3jrsleft', 's4jrsleft', 's5jrsleft']

# SECTION I: RETIREMENT (16 features)
# Whether Retired: Retirement year, if says retired
Retire1=['r2retyr', 'r3retyr', 'r4retyr', 'r5retyr', 's2retyr', 's3retyr', 's4retyr', 's5retyr']
# Whether Retired: Retirement age, if says retired
Retire2=['r2retage', 'r3retage', 'r4retage', 'r5retage', 's2retage', 's3retage', 's4retage', 's5retage']

# SECTION J: PENSION (54 features)
# Whether Receives Public Pension
Pension1=['r1pubpen', 'r2pubpen', 'r3pubpen', 'r4pubpen', 'r5pubpen', 's1pubpen', 's2pubpen', 's3pubpen', 's4pubpen', 's5pubpen']
# Whether Receives Private Pension
Pension2=['r1peninc', 'r2peninc', 'r3peninc', 'r4peninc', 'r5peninc', 's1peninc', 's2peninc', 's3peninc', 's4peninc', 's5peninc']
# Whether Receives Other Pension
Pension3=['r1open', 'r2open', 'r3open', 'r4open', 'r5open', 's1open', 's2open', 's3open', 's4open', 's5open']
# Age When Started to Receive a Public Pension
Pension4=['r1pubage', 'r2pubage', 'r5pubage', 's1pubage', 's2pubage', 's5pubage']
# Age When Started to Receive a Private Pension
Pension5=['r1penage', 'r2penage', 'r5penage', 's1penage', 's2penage', 's5penage']
# Whether Current Public Pension(s) Can Continue
Pension6=['r1ssic', 'r2ssic', 'r5ssic', 's1ssic', 's2ssic', 's5ssic']
# Whether Current Private Pension Can Continue
Pension7=['r1penic', 'r2penic', 'r5penic', 's1penic', 's2penic', 's5penic']

# SECTION K: PHYSICAL MEASURES (282 features)
# Height, Weight, Waist and Hip Circumference Measurements
Physic1 = ['r1mheight', 'r2mheight', 'r3mheight', 's1mheight', 's2mheight', 's3mheight', 'r1htcomp', 'r2htcomp', 'r3htcomp', 's1htcomp', 's2htcomp', 's3htcomp', 'r1mweight', 'r2mweight', 'r3mweight', 's1mweight', 's2mweight', 's3mweight', 'r1wtcomp', 'r2wtcomp', 'r3wtcomp', 's1wtcomp', 's2wtcomp', 's3wtcomp', 'r1mbmi', 'r2mbmi', 'r3mbmi', 's1mbmi', 's2mbmi', 's3mbmi', 'r1mbmicat', 'r2mbmicat', 'r3mbmicat', 's1mbmicat', 's2mbmicat', 's3mbmicat', 'r1mwaist', 'r2mwaist', 'r3mwaist', 's1mwaist', 's2mwaist', 's3mwaist', 'r1watcomp', 'r2watcomp', 'r3watcomp', 's1watcomp', 's2watcomp', 's3watcomp', 'r1mhip', 'r2mhip', 'r3mhip', 's1mhip', 's2mhip', 's3mhip', 'r1hipcomp', 'r2hipcomp', 'r3hipcomp', 's1hipcomp', 's2hipcomp', 's3hipcomp', 'r1mwhratio', 'r2mwhratio', 'r3mwhratio', 's1mwhratio', 's2mwhratio', 's3mwhratio']
# Height, Weight, Waist and Hip Circumference Measurements: Reason Didn't Complete
Physic2 = ['r1hghtsft', 'r2hghtsft', 'r3hghtsft', 's1hghtsft', 's2hghtsft', 's3hghtsft', 'r1hghttryu', 'r2hghttryu', 'r3hghttryu', 's1hghttryu', 's2hghttryu', 's3hghttryu', 'r1hghtref', 'r2hghtref', 'r3hghtref', 's1hghtref', 's2hghtref', 's3hghtref', 'r1wghtsft', 'r2wghtsft', 'r3wghtsft', 's1wghtsft', 's2wghtsft', 's3wghtsft', 'r1wghttryu', 'r2wghttryu', 'r3wghttryu', 's1wghttryu', 's2wghttryu', 's3wghttryu', 'r1wghtref', 'r2wghtref', 'r3wghtref', 's1wghtref', 's2wghtref', 's3wghtref', 'r1wstsft', 'r2wstsft', 'r3wstsft', 's1wstsft', 's2wstsft', 's3wstsft', 'r1wsttryu', 'r2wsttryu', 'r3wsttryu', 's1wsttryu', 's2wsttryu', 's3wsttryu', 'r1wstref', 'r2wstref', 'r3wstref', 's1wstref', 's2wstref', 's3wstref', 'r1hipsft', 'r2hipsft', 'r3hipsft', 's1hipsft', 's2hipsft', 's3hipsft', 'r1hiptryu', 'r2hiptryu', 'r3hiptryu', 's1hiptryu', 's2hiptryu', 's3hiptryu', 'r1hipref', 'r2hipref', 'r3hipref', 's1hipref', 's2hipref', 's3hipref']
# Sitting Height
Physic3 = ['r2sithght', 'r3sithght', 's2sithght', 's3sithght', 'r2chairhght', 'r3chairhght', 's2chairhght', 's3chairhght', 'r2sthtcomp', 'r3sthtcomp', 's2sthtcomp', 's3sthtcomp']
# Sitting Height: Reason Didn't Complete
Physic4 = ['r2sthtsft', 'r3sthtsft', 's2sthtsft', 's3sthtsft', 'r2sthttryu', 'r3sthttryu', 's2sthttryu', 's3sthttryu', 'r2sthtref', 'r3sthtref', 's2sthtref', 's3sthtref']
# Balance Test
Physic5 = ['r1balrtsec', 'r2balrtsec', 'r3balrtsec', 's1balrtsec', 's2balrtsec', 's3balrtsec', 'r1balrt', 'r2balrt', 'r3balrt', 's1balrt', 's2balrt', 's3balrt', 'r1balrtcomp', 'r2balrtcomp', 'r3balrtcomp', 's1balrtcomp', 's2balrtcomp', 's3balrtcomp', 'r1ballfsec', 'r2ballfsec', 'r3ballfsec', 's1ballfsec', 's2ballfsec', 's3ballfsec', 'r1ballf', 'r2ballf', 'r3ballf', 's1ballf', 's2ballf', 's3ballf', 'r1ballfcomp', 'r2ballfcomp', 'r3ballfcomp', 's1ballfcomp', 's2ballfcomp', 's3ballfcomp']
# Balance Test: Reason Didn't Complete
Physic6 = ['r1balsft', 'r2balsft', 'r3balsft', 's1balsft', 's2balsft', 's3balsft', 'r1balref', 'r2balref', 'r3balref', 's1balref', 's2balref', 's3balref', 'r1baltryu', 'r2baltryu', 'r3baltryu', 's1baltryu', 's2baltryu', 's3baltryu']
# Blood Pressure Measurements
Physic7 = ['r3systo1', 's3systo1', 'r3systo2', 's3systo2', 'r3systo', 's3systo', 'r3diasto1', 's3diasto1', 'r3diasto2', 's3diasto2', 'r3diasto', 's3diasto', 'r3pulse1', 's3pulse1', 'r3pulse2', 's3pulse2', 'r3pulse', 's3pulse', 'r3bpcomp', 's3bpcomp']
# Blood Pressure Measurements: Reason Didn't Complete
Physic8 = ['r3bpsft', 's3bpsft', 'r3bpref', 's3bpref']
# Timed Walk Measurements
Physic9 = ['r3wspeed1', 's3wspeed1', 'r3wspeed2', 's3wspeed2', 'r3wspeed', 's3wspeed', 'r3walkcomp', 's3walkcomp', 'r3walkaid_m', 's3walkaid_m']
# Timed Walk Measurements: Reason Didn't Complete
Physic10 = ['r3walksft', 's3walksft', 'r3walktryu', 's3walktryu', 'r3walkref', 's3walkref', 'r3walkothr', 's3walkothr']
# Hand Grip Strength Measurements
Physic11 = ['r3domhand', 's3domhand', 'r3rgrip1', 's3rgrip1', 'r3rgrip2', 's3rgrip2', 'r3rgrip', 's3rgrip', 'r3lgrip1', 's3lgrip1', 'r3lgrip2', 's3lgrip2', 'r3lgrip', 's3lgrip', 'r3gripsum', 's3gripsum', 'r3gripcomp', 's3gripcomp']
# Hand Grip Strength Measurements: Reason Didn't Complete
Physic12 = ['r3gripsft', 's3gripsft', 'r3gripref', 's3gripref', 'r3gripothr', 's3gripothr']

# SECTION L: ASSISTANCE AND CAREGIVING (1103 features)
# ADL Help
Assitan1 = ['r1dresshlp', 'r2dresshlp', 'r3dresshlp', 'r4dresshlp', 'r5dresshlp', 's1dresshlp', 's2dresshlp', 's3dresshlp', 's4dresshlp', 's5dresshlp', 'r1walkhlp', 'r2walkhlp', 'r3walkhlp', 'r4walkhlp', 'r5walkhlp', 's1walkhlp', 's2walkhlp', 's3walkhlp', 's4walkhlp', 's5walkhlp', 'r1bathehlp', 'r2bathehlp', 'r3bathehlp', 'r4bathehlp', 'r5bathehlp', 's1bathehlp', 's2bathehlp', 's3bathehlp', 's4bathehlp', 's5bathehlp', 'r1eathlp', 'r2eathlp', 'r3eathlp', 'r4eathlp', 'r5eathlp', 's1eathlp', 's2eathlp', 's3eathlp', 's4eathlp', 's5eathlp', 'r1bedhlp', 'r2bedhlp', 'r3bedhlp', 'r4bedhlp', 'r5bedhlp', 's1bedhlp', 's2bedhlp', 's3bedhlp', 's4bedhlp', 's5bedhlp', 'r1toilethlp', 'r2toilethlp', 'r3toilethlp', 'r4toilethlp', 'r5toilethlp', 's1toilethlp', 's2toilethlp', 's3toilethlp', 's4toilethlp', 's5toilethlp']
# IADL Help
Assitan2=['r1mealhlp', 'r2mealhlp', 'r3mealhlp', 'r4mealhlp', 'r5mealhlp', 's1mealhlp', 's2mealhlp', 's3mealhlp', 's4mealhlp', 's5mealhlp', 'r1shophlp', 'r2shophlp', 'r3shophlp', 'r4shophlp', 'r5shophlp', 's1shophlp', 's2shophlp', 's3shophlp', 's4shophlp', 's5shophlp', 'r1medhlp', 'r2medhlp', 'r3medhlp', 'r4medhlp', 'r5medhlp', 's1medhlp', 's2medhlp', 's3medhlp', 's4medhlp', 's5medhlp', 'r1moneyhlp', 'r2moneyhlp', 'r3moneyhlp', 'r4moneyhlp', 'r5moneyhlp', 's1moneyhlp', 's2moneyhlp', 's3moneyhlp', 's4moneyhlp', 's5moneyhlp']
# Whether Uses Personal Aids
Assitan3=['r1walkre', 'r2walkre', 'r3walkre', 'r4walkre', 'r5walkre', 's1walkre', 's2walkre', 's3walkre', 's4walkre', 's5walkre', 'r1bede', 'r2bede', 'r3bede', 'r4bede', 'r5bede', 's1bede', 's2bede', 's3bede', 's4bede', 's5bede']
# Future ADL Help
Assitan4=['r3ftrhlp', 'r4ftrhlp', 'r5ftrhlp', 's3ftrhlp', 's4ftrhlp', 's5ftrhlp']
# Activities of Daily Living: Whether Receives Any Care
Assitan5=['r1racany', 'r2racany', 'r3racany', 'r4racany', 'r5racany', 's1racany', 's2racany', 's3racany', 's4racany', 's5racany']
# Activities of Daily Living: Whether Receives Any Informal Care
Assitan6=['r1racaany', 'r2racaany', 'r3racaany', 'r4racaany', 'r5racaany', 's1racaany', 's2racaany', 's3racaany', 's4racaany', 's5racaany']
# Activities of Daily Living: Receives Informal Care from Spouse
Assitan7=['r1rascare', 'r2rascare', 'r3rascare', 'r4rascare', 'r5rascare', 's1rascare', 's2rascare', 's3rascare', 's4rascare', 's5rascare', 'r2rascaredpm', 'r3rascaredpm', 'r4rascaredpm', 'r5rascaredpm', 's2rascaredpm', 's3rascaredpm', 's4rascaredpm', 's5rascaredpm', 'r2rascaredpmm', 'r3rascaredpmm', 'r4rascaredpmm', 'r5rascaredpmm', 's2rascaredpmm', 's3rascaredpmm', 's4rascaredpmm', 's5rascaredpmm', 'r2rascarehr', 'r3rascarehr', 'r4rascarehr', 'r5rascarehr', 's2rascarehr', 's3rascarehr', 's4rascarehr', 's5rascarehr', 'r2rascarehrm', 'r3rascarehrm', 'r4rascarehrm', 'r5rascarehrm', 's2rascarehrm', 's3rascarehrm', 's4rascarehrm', 's5rascarehrm']
# Activities of Daily Living: Receives Informal Care from Children or Grandchildren
Assitan8=['r1raccare', 'r2raccare', 'r3raccare', 'r4raccare', 'r5raccare', 's1raccare', 's2raccare', 's3raccare', 's4raccare', 's5raccare', 'r1raccaren', 'r2raccaren', 'r3raccaren', 'r4raccaren', 'r5raccaren', 's1raccaren', 's2raccaren', 's3raccaren', 's4raccaren', 's5raccaren', 'r1raccaredpm', 'r2raccaredpm', 'r3raccaredpm', 'r4raccaredpm', 'r5raccaredpm', 's1raccaredpm', 's2raccaredpm', 's3raccaredpm', 's4raccaredpm', 's5raccaredpm', 'r1raccaredpmm', 'r2raccaredpmm', 'r3raccaredpmm', 'r4raccaredpmm', 'r5raccaredpmm', 's1raccaredpmm', 's2raccaredpmm', 's3raccaredpmm', 's4raccaredpmm', 's5raccaredpmm', 'r1raccarehr', 'r2raccarehr', 'r3raccarehr', 'r4raccarehr', 'r5raccarehr', 's1raccarehr', 's2raccarehr', 's3raccarehr', 's4raccarehr', 's5raccarehr', 'r1raccarehrm', 'r2raccarehrm', 'r3raccarehrm', 'r4raccarehrm', 'r5raccarehrm', 's1raccarehrm', 's2raccarehrm', 's3raccarehrm', 's4raccarehrm', 's5raccarehrm']
# Activities of Daily Living: Receives Informal Care from Relatives
Assitan9=['r1rarcare', 'r2rarcare', 'r3rarcare', 'r4rarcare', 'r5rarcare', 's1rarcare', 's2rarcare', 's3rarcare', 's4rarcare', 's5rarcare', 'r1rarcaren', 'r2rarcaren', 'r3rarcaren', 'r4rarcaren', 'r5rarcaren', 's1rarcaren', 's2rarcaren', 's3rarcaren', 's4rarcaren', 's5rarcaren', 'r1rarcaredpm', 'r2rarcaredpm', 'r3rarcaredpm', 'r4rarcaredpm', 'r5rarcaredpm', 's1rarcaredpm', 's2rarcaredpm', 's3rarcaredpm', 's4rarcaredpm', 's5rarcaredpm', 'r1rarcaredpmm', 'r2rarcaredpmm', 'r3rarcaredpmm', 'r4rarcaredpmm', 'r5rarcaredpmm', 's1rarcaredpmm', 's2rarcaredpmm', 's3rarcaredpmm', 's4rarcaredpmm', 's5rarcaredpmm', 'r1rarcarehr', 'r2rarcarehr', 'r3rarcarehr', 'r4rarcarehr', 'r5rarcarehr', 's1rarcarehr', 's2rarcarehr', 's3rarcarehr', 's4rarcarehr', 's5rarcarehr', 'r1rarcarehrm', 'r2rarcarehrm', 'r3rarcarehrm', 'r4rarcarehrm', 'r5rarcarehrm', 's1rarcarehrm', 's2rarcarehrm', 's3rarcarehrm', 's4rarcarehrm', 's5rarcarehrm']
# Activities of Daily Living: Receives Informal Care from Other Individuals
Assitan10=['r1rafcare', 'r2rafcare', 'r3rafcare', 'r4rafcare', 'r5rafcare', 's1rafcare', 's2rafcare', 's3rafcare', 's4rafcare', 's5rafcare', 'r1rafcaren', 'r2rafcaren', 'r3rafcaren', 'r4rafcaren', 'r5rafcaren', 's1rafcaren', 's2rafcaren', 's3rafcaren', 's4rafcaren', 's5rafcaren', 'r1rafcaredpm', 'r2rafcaredpm', 'r3rafcaredpm', 'r4rafcaredpm', 'r5rafcaredpm', 's1rafcaredpm', 's2rafcaredpm', 's3rafcaredpm', 's4rafcaredpm', 's5rafcaredpm', 'r1rafcaredpmm', 'r2rafcaredpmm', 'r3rafcaredpmm', 'r4rafcaredpmm', 'r5rafcaredpmm', 's1rafcaredpmm', 's2rafcaredpmm', 's3rafcaredpmm', 's4rafcaredpmm', 's5rafcaredpmm', 'r1rafcarehr', 'r2rafcarehr', 'r3rafcarehr', 'r4rafcarehr', 'r5rafcarehr', 's1rafcarehr', 's2rafcarehr', 's3rafcarehr', 's4rafcarehr', 's5rafcarehr', 'r1rafcarehrm', 'r2rafcarehrm', 'r3rafcarehrm', 'r4rafcarehrm', 'r5rafcarehrm', 's1rafcarehrm', 's2rafcarehrm', 's3rafcarehrm', 's4rafcarehrm', 's5rafcarehrm']
# Activities of Daily Living: Whether Receives Any Formal Care
Assitan11=['r1rafaany', 'r2rafaany', 'r3rafaany', 'r4rafaany', 'r5rafaany', 's1rafaany', 's2rafaany', 's3rafaany', 's4rafaany', 's5rafaany']
# Activities of Daily Living: Receives Formal Care from Paid Professional
Assitan12=['r1rapfcare', 'r2rapfcare', 'r3rapfcare', 'r4rapfcare', 'r5rapfcare', 's1rapfcare', 's2rapfcare', 's3rapfcare', 's4rapfcare', 's5rapfcare', 'r1rapfcaren', 'r2rapfcaren', 'r3rapfcaren', 'r4rapfcaren', 'r5rapfcaren', 's1rapfcaren', 's2rapfcaren', 's3rapfcaren', 's4rapfcaren', 's5rapfcaren', 'r1rapfcaredpm', 'r2rapfcaredpm', 'r3rapfcaredpm', 'r4rapfcaredpm', 'r5rapfcaredpm', 's1rapfcaredpm', 's2rapfcaredpm', 's3rapfcaredpm', 's4rapfcaredpm', 's5rapfcaredpm', 'r1rapfcaredpmm', 'r2rapfcaredpmm', 'r3rapfcaredpmm', 'r4rapfcaredpmm', 'r5rapfcaredpmm', 's1rapfcaredpmm', 's2rapfcaredpmm', 's3rapfcaredpmm', 's4rapfcaredpmm', 's5rapfcaredpmm', 'r1rapfcarehr', 'r2rapfcarehr', 'r3rapfcarehr', 'r4rapfcarehr', 'r5rapfcarehr', 's1rapfcarehr', 's2rapfcarehr', 's3rapfcarehr', 's4rapfcarehr', 's5rapfcarehr', 'r1rapfcarehrm', 'r2rapfcarehrm', 'r3rapfcarehrm', 'r4rapfcarehrm', 'r5rapfcarehrm', 's1rapfcarehrm', 's2rapfcarehrm', 's3rapfcarehrm', 's4rapfcarehrm', 's5rapfcarehrm']
# Instrumental Activities of Daily Living: Whether Receives Any Care
Assitan13=['r1ricany', 'r2ricany', 'r3ricany', 'r4ricany', 'r5ricany', 's1ricany', 's2ricany', 's3ricany', 's4ricany', 's5ricany']
# Instrumental Activities of Daily Living: Whether Receives Any Informal Care
Assitan14=['r1ricaany', 'r2ricaany', 'r3ricaany', 'r4ricaany', 'r5ricaany', 's1ricaany', 's2ricaany', 's3ricaany', 's4ricaany', 's5ricaany']
# Instrumental Activities of Daily Living: Receives Informal Care from Spouse
Assitan15=['r1riscare', 'r2riscare', 'r3riscare', 'r4riscare', 'r5riscare', 's1riscare', 's2riscare', 's3riscare', 's4riscare', 's5riscare', 'r2riscaredpm', 'r3riscaredpm', 'r4riscaredpm', 'r5riscaredpm', 's2riscaredpm', 's3riscaredpm', 's4riscaredpm', 's5riscaredpm', 'r2riscaredpmm', 'r3riscaredpmm', 'r4riscaredpmm', 'r5riscaredpmm', 's2riscaredpmm', 's3riscaredpmm', 's4riscaredpmm', 's5riscaredpmm', 'r2riscarehr', 'r3riscarehr', 'r4riscarehr', 'r5riscarehr', 's2riscarehr', 's3riscarehr', 's4riscarehr', 's5riscarehr', 'r2riscarehrm', 'r3riscarehrm', 'r4riscarehrm', 'r5riscarehrm', 's2riscarehrm', 's3riscarehrm', 's4riscarehrm', 's5riscarehrm']
# Instrumental Activities of Daily Living: Receives Informal Care from Children or Grandchildren
Assitan16=['r1riccare', 'r2riccare', 'r3riccare', 'r4riccare', 'r5riccare', 's1riccare', 's2riccare', 's3riccare', 's4riccare', 's5riccare', 'r1riccaren', 'r2riccaren', 'r3riccaren', 'r4riccaren', 'r5riccaren', 's1riccaren', 's2riccaren', 's3riccaren', 's4riccaren', 's5riccaren', 'r1riccaredpm', 'r2riccaredpm', 'r3riccaredpm', 'r4riccaredpm', 'r5riccaredpm', 's1riccaredpm', 's2riccaredpm', 's3riccaredpm', 's4riccaredpm', 's5riccaredpm', 'r1riccaredpmm', 'r2riccaredpmm', 'r3riccaredpmm', 'r4riccaredpmm', 's1riccaredpmm', 's2riccaredpmm', 's3riccaredpmm', 's4riccaredpmm', 's5riccaredpmm', 'r1riccarehr', 'r2riccarehr', 'r3riccarehr', 'r4riccarehr', 'r5riccarehr', 's1riccarehr', 's2riccarehr', 's3riccarehr', 's4riccarehr', 's5riccarehr', 'r1riccarehrm', 'r2riccarehrm', 'r3riccarehrm', 'r4riccarehrm', 'r5riccarehrm', 's1riccarehrm', 's2riccarehrm', 's3riccarehrm', 's4riccarehrm', 's5riccarehrm']
# Instrumental Activities of Daily Living: Receives Informal Care from Relatives
Assitan17=['r1rircare', 'r2rircare', 'r3rircare', 'r4rircare', 'r5rircare', 's1rircare', 's2rircare', 's3rircare', 's4rircare', 's5rircare', 'r1rircaren', 'r2rircaren', 'r3rircaren', 'r4rircaren', 'r5rircaren', 's1rircaren', 's2rircaren', 's3rircaren', 's4rircaren', 's5rircaren', 'r1rircaredpm', 'r2rircaredpm', 'r3rircaredpm', 'r4rircaredpm', 'r5rircaredpm', 's1rircaredpm', 's2rircaredpm', 's3rircaredpm', 's4rircaredpm', 's5rircaredpm', 'r1rircaredpmm', 'r2rircaredpmm', 'r3rircaredpmm', 'r4rircaredpmm', 'r5rircaredpmm', 's1rircaredpmm', 's2rircaredpmm', 's3rircaredpmm', 's4rircaredpmm', 's5rircaredpmm', 'r1rircarehr', 'r2rircarehr', 'r3rircarehr', 'r4rircarehr', 'r5rircarehr', 's1rircarehr', 's2rircarehr', 's3rircarehr', 's4rircarehr', 's5rircarehr', 'r1rircarehrm', 'r2rircarehrm', 'r3rircarehrm', 'r4rircarehrm', 'r5rircarehrm', 's1rircarehrm', 's2rircarehrm', 's3rircarehrm', 's4rircarehrm', 's5rircarehrm']
# Instrumental Activities of Daily Living: Receives Informal Care from Other Individuals
Assitan18=['r1rifcare', 'r2rifcare', 'r3rifcare', 'r4rifcare', 'r5rifcare', 's1rifcare', 's2rifcare', 's3rifcare', 's4rifcare', 's5rifcare', 'r1rifcaren', 'r2rifcaren', 'r3rifcaren', 'r4rifcaren', 'r5rifcaren', 's1rifcaren', 's2rifcaren', 's3rifcaren', 's4rifcaren', 's5rifcaren', 'r1rifcaredpm', 'r2rifcaredpm', 'r3rifcaredpm', 'r4rifcaredpm', 'r5rifcaredpm', 's1rifcaredpm', 's2rifcaredpm', 's3rifcaredpm', 's4rifcaredpm', 's5rifcaredpm', 'r1rifcaredpmm', 'r2rifcaredpmm', 'r3rifcaredpmm', 'r4rifcaredpmm', 'r5rifcaredpmm', 's1rifcaredpmm', 's2rifcaredpmm', 's3rifcaredpmm', 's4rifcaredpmm', 's5rifcaredpmm', 'r1rifcarehr', 'r2rifcarehr', 'r3rifcarehr', 'r4rifcarehr', 'r5rifcarehr', 's1rifcarehr', 's2rifcarehr', 's3rifcarehr', 's4rifcarehr', 's5rifcarehr', 'r1rifcarehrm', 'r2rifcarehrm', 'r3rifcarehrm', 'r4rifcarehrm', 'r5rifcarehrm', 's1rifcarehrm', 's2rifcarehrm', 's3rifcarehrm', 's4rifcarehrm', 's5rifcarehrm']
# Instrumental Activities of Daily Living: Whether Receives Any Formal Care
Assitan19=['r1rifaany', 'r2rifaany', 'r3rifaany', 'r4rifaany', 'r5rifaany', 's1rifaany', 's2rifaany', 's3rifaany', 's4rifaany', 's5rifaany']
# Instrumental Activities of Daily Living: Receives Formal Care from Paid Professional
Assitan20=['r1ripfcare', 'r2ripfcare', 'r3ripfcare', 'r4ripfcare', 'r5ripfcare', 's1ripfcare', 's2ripfcare', 's3ripfcare', 's4ripfcare', 's5ripfcare', 'r1ripfcaren', 'r2ripfcaren', 'r3ripfcaren', 'r4ripfcaren', 'r5ripfcaren', 's1ripfcaren', 's2ripfcaren', 's3ripfcaren', 's4ripfcaren', 's5ripfcaren', 'r1ripfcaredpm', 'r2ripfcaredpm', 'r3ripfcaredpm', 'r4ripfcaredpm', 'r5ripfcaredpm', 's1ripfcaredpm', 's2ripfcaredpm', 's3ripfcaredpm', 's4ripfcaredpm', 's5ripfcaredpm', 'r1ripfcaredpmm', 'r2ripfcaredpmm', 'r3ripfcaredpmm', 'r4ripfcaredpmm', 'r5ripfcaredpmm', 's1ripfcaredpmm', 's2ripfcaredpmm', 's3ripfcaredpmm', 's4ripfcaredpmm', 's5ripfcaredpmm', 'r1ripfcarehr', 'r2ripfcarehr', 'r3ripfcarehr', 'r4ripfcarehr', 'r5ripfcarehr', 's1ripfcarehr', 's2ripfcarehr', 's3ripfcarehr', 's4ripfcarehr', 's5ripfcarehr', 'r1ripfcarehrm', 'r2ripfcarehrm', 'r3ripfcarehrm', 'r4ripfcarehrm', 'r5ripfcarehrm', 's1ripfcarehrm', 's2ripfcarehrm', 's3ripfcarehrm', 's4ripfcarehrm', 's5ripfcarehrm']
# Activities of Daily Living and Instrumental Activities of Daily Living: Whether Receives Any Care
Assitan21=['r1rcany', 'r2rcany', 'r3rcany', 'r4rcany', 'r5rcany', 's1rcany', 's2rcany', 's3rcany', 's4rcany', 's5rcany']
# Activities of Daily Living and Instrumental Activities of Daily Living: Whether Receives Any Informal Care
Assitan22=['r1rcaany', 'r2rcaany', 'r3rcaany', 'r4rcaany', 'r5rcaany', 's1rcaany', 's2rcaany', 's3rcaany', 's4rcaany', 's5rcaany']
# Activities of Daily Living and Instrumental Activities of Daily Living: Receives Informal Care from Spouse
Assitan23=['r1rscare', 'r2rscare', 'r3rscare', 'r4rscare', 'r5rscare', 's1rscare', 's2rscare', 's3rscare', 's4rscare', 's5rscare', 'r2rscaredpm', 'r3rscaredpm', 'r4rscaredpm', 'r5rscaredpm', 's2rscaredpm', 's3rscaredpm', 's4rscaredpm', 's5rscaredpm', 'r2rscaredpmm', 'r3rscaredpmm', 'r4rscaredpmm', 'r5rscaredpmm', 's2rscaredpmm', 's3rscaredpmm', 's4rscaredpmm', 's5rscaredpmm', 'r2rscarehr', 'r3rscarehr', 'r4rscarehr', 'r5rscarehr', 's2rscarehr', 's3rscarehr', 's4rscarehr', 's5rscarehr', 'r2rscarehrm', 'r3rscarehrm', 'r4rscarehrm', 'r5rscarehrm', 's2rscarehrm', 's3rscarehrm', 's4rscarehrm', 's5rscarehrm']
# Activities of Daily Living and Instrumental Activities of Daily Living: Receives Informal Care from Children or Grandchildren
Assitan24=['r1rccare', 'r2rccare', 'r3rccare', 'r4rccare', 'r5rccare', 's1rccare', 's2rccare', 's3rccare', 's4rccare', 's5rccare', 'r1rccaren', 'r2rccaren', 'r3rccaren', 'r4rccaren', 'r5rccaren', 's1rccaren', 's2rccaren', 's3rccaren', 's4rccaren', 's5rccaren', 'r1rccaredpm', 'r2rccaredpm', 'r3rccaredpm', 'r4rccaredpm', 'r5rccaredpm', 's1rccaredpm', 's2rccaredpm', 's3rccaredpm', 's4rccaredpm', 's5rccaredpm', 'r1rccaredpmm', 'r2rccaredpmm', 'r3rccaredpmm', 'r4rccaredpmm', 'r5rccaredpmm', 's1rccaredpmm', 's2rccaredpmm', 's3rccaredpmm', 's4rccaredpmm', 's5rccaredpmm', 'r1rccarehr', 'r2rccarehr', 'r3rccarehr', 'r4rccarehr', 'r5rccarehr', 's1rccarehr', 's2rccarehr', 's3rccarehr', 's4rccarehr', 's5rccarehr', 'r1rccarehrm', 'r2rccarehrm', 'r3rccarehrm', 'r4rccarehrm', 'r5rccarehrm', 's1rccarehrm', 's2rccarehrm', 's3rccarehrm', 's4rccarehrm', 's5rccarehrm']
# Activities of Daily Living and Instrumental Activities of Daily Living: Receives Informal Care from Relatives
Assitan25=['r1rrcare', 'r2rrcare', 'r3rrcare', 'r4rrcare', 'r5rrcare', 's1rrcare', 's2rrcare', 's3rrcare', 's4rrcare', 's5rrcare', 'r1rrcaren', 'r2rrcaren', 'r3rrcaren', 'r4rrcaren', 'r5rrcaren', 's1rrcaren', 's2rrcaren', 's3rrcaren', 's4rrcaren', 's5rrcaren', 'r1rrcaredpm', 'r2rrcaredpm', 'r3rrcaredpm', 'r4rrcaredpm', 'r5rrcaredpm', 's1rrcaredpm', 's2rrcaredpm', 's3rrcaredpm', 's4rrcaredpm', 's5rrcaredpm', 'r1rrcaredpmm', 'r2rrcaredpmm', 'r3rrcaredpmm', 'r4rrcaredpmm', 'r5rrcaredpmm', 's1rrcaredpmm', 's2rrcaredpmm', 's3rrcaredpmm', 's4rrcaredpmm', 's5rrcaredpmm', 'r1rrcarehr', 'r2rrcarehr', 'r3rrcarehr', 'r4rrcarehr', 'r5rrcarehr', 's1rrcarehr', 's2rrcarehr', 's3rrcarehr', 's4rrcarehr', 's5rrcarehr', 'r1rrcarehrm', 'r2rrcarehrm', 'r3rrcarehrm', 'r4rrcarehrm', 'r5rrcarehrm', 's1rrcarehrm', 's2rrcarehrm', 's3rrcarehrm', 's4rrcarehrm', 's5rrcarehrm']
# Activities of Daily Living and Instrumental Activities of Daily Living: Receives Informal Care from Other Individuals
Assitan26=['r1rfcare', 'r2rfcare', 'r3rfcare', 'r4rfcare', 'r5rfcare', 's1rfcare', 's2rfcare', 's3rfcare', 's4rfcare', 's5rfcare', 'r1rfcaren', 'r2rfcaren', 'r3rfcaren', 'r4rfcaren', 'r5rfcaren', 's1rfcaren', 's2rfcaren', 's3rfcaren', 's4rfcaren', 's5rfcaren', 'r1rfcaredpm', 'r2rfcaredpm', 'r3rfcaredpm', 'r4rfcaredpm', 'r5rfcaredpm', 's1rfcaredpm', 's2rfcaredpm', 's3rfcaredpm', 's4rfcaredpm', 's5rfcaredpm', 'r1rfcaredpmm', 'r2rfcaredpmm', 'r3rfcaredpmm', 'r4rfcaredpmm', 'r5rfcaredpmm', 's1rfcaredpmm', 's2rfcaredpmm', 's3rfcaredpmm', 's4rfcaredpmm', 's5rfcaredpmm', 'r1rfcarehr', 'r2rfcarehr', 'r3rfcarehr', 'r4rfcarehr', 'r5rfcarehr', 's1rfcarehr', 's2rfcarehr', 's3rfcarehr', 's4rfcarehr', 's5rfcarehr', 'r1rfcarehrm', 'r2rfcarehrm', 'r3rfcarehrm', 'r4rfcarehrm', 'r5rfcarehrm', 's1rfcarehrm', 's2rfcarehrm', 's3rfcarehrm', 's4rfcarehrm', 's5rfcarehrm']
# Activities of Daily Living and Instrumental Activities of Daily Living: Whether Receives Any Formal Care
Assitan27=['r1rfaany', 'r2rfaany', 'r3rfaany', 'r4rfaany', 'r5rfaany', 's1rfaany', 's2rfaany', 's3rfaany', 's4rfaany', 's5rfaany']
# Activities of Daily Living and Instrumental Activities of Daily Living: Receives Formal Care from Paid Professional
Assitan28=['r1rpfcare', 'r2rpfcare', 'r3rpfcare', 'r4rpfcare', 'r5rpfcare', 's1rpfcare', 's2rpfcare', 's3rpfcare', 's4rpfcare', 's5rpfcare', 'r1rpfcaren', 'r2rpfcaren', 'r3rpfcaren', 'r4rpfcaren', 'r5rpfcaren', 's1rpfcaren', 's2rpfcaren', 's3rpfcaren', 's4rpfcaren', 's5rpfcaren', 'r1rpfcaredpm', 'r2rpfcaredpm', 'r3rpfcaredpm', 'r4rpfcaredpm', 'r5rpfcaredpm', 's2rpfcaredpm', 's3rpfcaredpm', 's4rpfcaredpm', 's5rpfcaredpm', 'r1rpfcaredpmm', 'r2rpfcaredpmm', 'r3rpfcaredpmm', 'r4rpfcaredpmm', 'r5rpfcaredpmm', 's1rpfcaredpmm', 's2rpfcaredpmm', 's3rpfcaredpmm', 's4rpfcaredpmm', 's5rpfcaredpmm', 'r1rpfcarehr', 'r2rpfcarehr', 'r3rpfcarehr', 'r4rpfcarehr', 'r5rpfcarehr', 's1rpfcarehr', 's2rpfcarehr', 's3rpfcarehr', 's4rpfcarehr', 's5rpfcarehr', 'r1rpfcarehrm', 'r2rpfcarehrm', 'r3rpfcarehrm', 'r4rpfcarehrm', 'r5rpfcarehrm', 's1rpfcarehrm', 's2rpfcarehrm', 's3rpfcarehrm', 's4rpfcarehrm', 's5rpfcarehrm']
# Receives Help with Chores from Children or Grandchildren
Assitan29=['h1rcchore', 'h2rcchore', 'h3rcchore', 'h4rcchore', 'h5rcchore', 'h2rcchorenf', 'h3rcchorenf', 'h4rcchorenf', 'h5rcchorenf', 'h3rcchorehr', 'h4rcchorehr', 'h5rcchorehr']
# Provides Informal Care to Children or Grandchildren
Assitan30=['h1gccare_m', 'h2gccare_m', 'h3gccare_m', 'h4gccare_m', 'h5gccare_m', 'h1gccarehr_m', 'h2gccarehr_m', 'h3gccarehr_m', 'h4gccarehr_m', 'h5gccarehr_m']
# Provides Personal Care to Parents
Assitan31=['h1gapcare', 'h2gapcare', 'h3gapcare', 'h4gapcare', 'h5gapcare', 'h1gapcarehr', 'h2gapcarehr', 'h3gapcarehr', 'h4gapcarehr']
# Provides Informal Care for Sick or Disabled Adults
Assitan32=['r3gcaresck', 'r4gcaresck', 'r5gcaresck', 's3gcaresck', 's4gcaresck', 's5gcaresck', 'r3gcaresckd_m', 'r4gcaresckd_m', 'r5gcaresckd_m', 's3gcaresckd_m', 's4gcaresckd_m', 's5gcaresckd_m']

# SECTION M: STRESS (77 features)
# Social Support: Spouse
Stress1 = ['r2sustdfe_m', 'r3sustdfe_m', 's2sustdfe_m', 's3sustdfe_m', 'r2srely_m', 'r3srely_m', 's2srely_m', 's3srely_m', 'r2sopenup_m', 'r3sopenup_m', 's2sopenup_m', 's3sopenup_m', 'r2sletdow_m', 'r3sletdow_m', 's2sletdow_m', 's3sletdow_m', 'r2ssupport4_m', 'r3ssupport4_m', 's2ssupport4_m', 's3ssupport4_m', 'r2ssupport4m_m', 'r3ssupport4m_m', 's2ssupport4m_m', 's3ssupport4m_m']
# Social Support: Children
Stress2 = ['r2kustdfe_m', 'r3kustdfe_m', 's2kustdfe_m', 's3kustdfe_m', 'r2krely_m', 'r3krely_m', 's2krely_m', 's3krely_m', 'r2kopenup_m', 'r3kopenup_m', 's2kopenup_m', 's3kopenup_m', 'r2kletdow_m', 'r3kletdow_m', 's2kletdow_m', 's3kletdow_m', 'r2ksupport4_m', 'r3ksupport4_m', 's2ksupport4_m', 's3ksupport4_m', 'r2ksupport4m_m', 'r3ksupport4m_m', 's2ksupport4m_m', 's3ksupport4m_m']
# Social Support: Friends
Stress3 = ['r2fustdfe_m', 'r3fustdfe_m', 's2fustdfe_m', 's3fustdfe_m', 'r2frely_m', 'r3frely_m', 's2frely_m', 's3frely_m', 'r2fopenup_m', 'r3fopenup_m', 's2fopenup_m', 's3fopenup_m', 'r2fletdow_m', 'r3fletdow_m', 's2fletdow_m', 's3fletdow_m', 'r2fsupport4_m', 'r3fsupport4_m', 's2fsupport4_m', 's3fsupport4_m', 'r2fsupport4m_m', 'r3fsupport4m_m', 's2fsupport4m_m', 's3fsupport4m_m']
# Experienced Death of a Child
Stress4 = ['h1chdeathe', 'h2chdeathe', 'h3chdeathe', 'h4chdeathe', 'h5chdeathe']

# SECTION O: END OF LIFE PLANNING (33 features)
# Will: Whether Has a Will
Plannin1 = ['h1witwill_m', 'h2witwill_m', 'h3witwill_m', 'h4witwill_m', 'h5witwill_m', 'h3witwill', 'h4witwill', 'h5witwill']
# Will: Beneficiaries of Will
Plannin2 = ['h1willsp', 'h2willsp', 'h3willsp', 'h4willsp', 'h5willsp', 'h1willcg', 'h2willcg', 'h3willcg', 'h4willcg', 'h5willcg', 'h1willot', 'h2willot', 'h3willot', 'h4willot', 'h5willot']
# Covered by Life Insurance
Plannin3 = ['r1lifein_m', 'r2lifein_m', 'r3lifein_m', 'r4lifein_m', 'r5lifein_m', 's1lifein_m', 's2lifein_m', 's3lifein_m', 's4lifein_m', 's5lifein_m']

# SECTION Q: PSYCHOSOCIAL (166 features)
# Depressive Symptoms: CESD
Phychos1 = ['r1depres', 'r2depres', 'r3depres', 'r4depres', 'r5depres', 's1depres', 's2depres', 's3depres', 's4depres', 's5depres', 'r1effort', 'r2effort', 'r3effort', 'r4effort', 'r5effort', 's1effort', 's2effort', 's3effort', 's4effort', 's5effort', 'r1sleepr', 'r2sleepr', 'r3sleepr', 'r4sleepr', 'r5sleepr', 's1sleepr', 's2sleepr', 's3sleepr', 's4sleepr', 's5sleepr', 'r1whappy', 'r2whappy', 'r3whappy', 'r4whappy', 'r5whappy', 's1whappy', 's2whappy', 's3whappy', 's4whappy', 's5whappy', 'r1flone', 'r2flone', 'r3flone', 'r4flone', 'r5flone', 's1flone', 's2flone', 's3flone', 's4flone', 's5flone', 'r1enlife', 'r2enlife', 'r3enlife', 'r4enlife', 'r5enlife', 's1enlife', 's2enlife', 's3enlife', 's4enlife', 's5enlife', 'r1fsad', 'r2fsad', 'r3fsad', 'r4fsad', 'r5fsad', 's1fsad', 's2fsad', 's3fsad', 's4fsad', 's5fsad', 'r1ftired', 'r2ftired', 'r3ftired', 'r4ftired', 'r5ftired', 's1ftired', 's2ftired', 's3ftired', 's4ftired', 's5ftired', 'r1energ', 'r2energ', 'r3energ', 'r4energ', 'r5energ', 's1energ', 's2energ', 's3energ', 's4energ', 's5energ', 'r1cesd_m', 'r2cesd_m', 'r3cesd_m', 'r4cesd_m', 'r5cesd_m', 's1cesd_m', 's2cesd_m', 's3cesd_m', 's4cesd_m', 's5cesd_m', 'r1cesdm_m', 'r2cesdm_m', 'r3cesdm_m', 'r4cesdm_m', 'r5cesdm_m', 's1cesdm_m', 's2cesdm_m', 's3cesdm_m', 's4cesdm_m', 's5cesdm_m']
# Satisfaction with Life Scale
Phychos2 = ['r3lideal3', 'r4lideal3', 'r5lideal3', 's3lideal3', 's4lideal3', 's5lideal3', 'r3lexcl3', 'r4lexcl3', 'r5lexcl3', 's3lexcl3', 's4lexcl3', 's5lexcl3', 'r3lstsf3', 'r4lstsf3', 'r5lstsf3', 's3lstsf3', 's4lstsf3', 's5lstsf3', 'r3limptt3', 'r4limptt3', 'r5limptt3', 's3limptt3', 's4limptt3', 's5limptt3', 'r3lchnot3', 'r4lchnot3', 'r5lchnot3', 's3lchnot3', 's4lchnot3', 's5lchnot3', 'r3lsatsc3', 'r4lsatsc3', 'r5lsatsc3', 's3lsatsc3', 's4lsatsc3', 's5lsatsc3', 'r3lsatsc3m', 'r4lsatsc3m', 'r5lsatsc3m', 's3lsatsc3m', 's4lsatsc3m', 's5lsatsc3m']
# Single Life Satisfaction Question
Phychos3 = ['r3satlife_m', 'r4satlife_m', 'r5satlife_m', 's3satlife_m', 's4satlife_m', 's5satlife_m', 'r3satlifez', 'r4satlifez', 'r5satlifez', 's3satlifez', 's4satlifez', 's5satlifez']
# Cantril Ladder
Phychos4 = ['r2cantril', 's2cantril']

section_A = {
    'Person Specific Identifier' : Demog1,
    'Household Identifier' : Demog2,
    'Spouse Identifier' : Demog3,
    'Response Indicator' : Demog4,
    'Interview Status' : Demog5,
    'Sample Cohort' : Demog6,
    'Whether Proxy Interview' : Demog7,
    'Number of Household Respondents' : Demog8,
    'Whether Couple Household' : Demog9,
    'Household Analysis Weight' : Demog10,
    'Person-Level Analysis Weight' :Demog11,
    'Interview Dates' : Demog12,
    'Birth Date' : Demog13,
    'Death Date' : Demog14,
    'Age at Interview' : Demog15,
    'Gender' : Demog16,
    'Education' : Demog17,
    'Education_Cat' : Demog18,
    'Education_ Harmon' : Demog19,
    'Literacy and Numeracy' : Demog20,
    'Indigenous Language' : Demog21,
    'Current Partnership Status' : Demog22,
    'With Partnership' : Demog23,
    'Without Partnership' : Demog24,
    'Number of Marriages' : Demog25,
    'Urban or Rural' : Demog26
}

section_B = {
    'Self-Report of Health' : Health1,
    'ADLs Raw Recodes' : Health2,
    'ADLs Some Difficulty' : Health3,
    'IADLs Raw Recodes' : Health4,
    'IADLs Some Difficulty' : Health5,
    'Other Limitations Raw Recodes' : Health6,
    'Other Limitations Some Difficulty' : Health7,
    'ADL Summary' : Health8,
    'IADL Summary' : Health9,
    'Other Summary Indices' : Health10,
    'Doctor Diagnosed Health Problems' : Health11,
    'Treatment or Medication for Disease' : Health12,
    'Whether Disease Limits Activity' : Health13,
    'Age of Diagnosis' : Health14,
    'Vision' : Health15,
    'Hearing' : Health16,
    'Falls' : Health17,
    'Urinary Incontinence' : Health18,
    'Persistent Health Problems' : Health19,
    'Sleep' : Health20,
    'Pain' : Health21,
    'Menopause' : Health22,
    'BMI' : Health23,
    'Physical Activity or Exercise' : Health24,
    'Drinking' : Health25,
    'Smoking (Cigarettes)' : Health26,
    'Preventive Care' : Health27
}

section_C = {
    'Medical Care Hospital' : HCare1,
    'Medical Care Doctor' : HCare2,
    'Medical Care Other' : HCare3,
    'Medical Expenditures' : HCare4,
    'Covered by Government' : HCare5,
    'Covered by Private' : HCare6,
    'Covered by Employer' : HCare7,
    'Number of Health Insurance Plans' : HCare8
}

section_D = {
    'Cognition Testing Conditions' : Cognit1,
    'Self-Reported Memory' : Cognit2,
    'Immediate Word Recall' : Cognit3,
    'Delayed Word Recall' : Cognit4,
    'Summary Scores' : Cognit5,
    'Picture Drawing' : Cognit6,
    'Verbal Fluency' : Cognit7,
    'Visual Scanning' : Cognit8,
    'Backwards Counting From 20' : Cognit9,
    'Date Naming/Orientation' : Cognit10,
    'Serial 7s' : Cognit11,
    'JORM IQCODE' : Cognit12,
    'Ratings of Memory and Abilities' : Cognit13,
    'Cognitive Impairment' : Cognit14,
    'Problem Behaviors in Past Week' : Cognit15
}

section_E = {
    'Inflation Multiplier' : Financ1,
    'Net Value of Real Estate' : Financ2,
    'Net Value of Cars' : Financ3,
    'Net Value of Businesses' : Financ4, 
    'Value of Stocks' : Financ5,
    'Value of Accounts' : Financ6,
    'Value of Other' : Financ7,
    'Value of Residence' : Financ8,
    'Value of Mortgages' : Financ9,
    'Net Value P Residence' : Financ10,
    'Home ownership' : Financ11,
    'Value of Other Debt' : Financ12,
    'Value of Loans Lent' : Financ13,
    'Net Value Financial Wealth' : Financ14,
    'Total Wealth' : Financ15
}

section_F = {
    'Individual Earnings' : Incom1,
    'Household Income' : Incom2,
    'Income from Private Pension' : Incom3,
    'Public Pension Income' : Incom4,
    'Other Pensions Income' : Incom5,
    'Total Pensions Income' : Incom6,
    'Other Government Transfers' : Incom7,
    'All Other Income' : Incom8,
    'Total Household Income r&s' : Incom9,
    'Total Household Consumption h' : Incom10
}

section_G = {
    'N Living in Household' : Family1,
    'N Living Children' : Family2,
    'N Deceased Children' : Family3,
    'N Children Ever Born' : Family4,
    'N Grandchildren' : Family5,
    'N Living Siblings' : Family6,
    'N Deceased Siblings' : Family7,
    'N Living Parents' : Family8,
    'Parental Mortality' : Family9,
    'Parents Age or Age at Death' : Family10,
    'Parents Education' : Family11,
    'Any Child with Respondent' : Family12,
    'Any Children Same City' : Family13,
    'Any Weekly Contact with Children' : Family14,
    'Frequent Contact with Relatives' : Family15,
    'Weekly Social Activities' : Family16,
    'Financial Transfer from Children' : Family17,
    'Financial Transfer to Children' : Family18,
    'Financial Transfer to Parents' : Family19
}

section_H = {
    'Currently Working for Pay' : Employ1,
    'Whether Self-Employed' : Employ2,
    'Labor Force Status' : Employ3,
    'In the Labor Force' : Employ4,
    'Unemployment Status' : Employ5,
    'Retired Employment Status' : Employ6,
    'Hours at Main Job' : Employ7,
    'Main Activity Years of Tenure' : Employ8,
    'Job Allows Move' : Employ9,
    'Occupation Code with Longest' : Employ10,
    'Year Last Job Ended' : Employ11,
    'Reason Job Ended' : Employ12
}

section_I = {
    'Retirement year' : Retire1,
    'Retirement age' : Retire2
}

section_J = {
    'Public Pension' : Pension1,
    'Private Pension' : Pension2,
    'Other Pension' : Pension3,
    'Age Public Pension' : Pension4,
    'Age Private Pension' : Pension5,
    'Public Pension Continuity' : Pension6,
    'Private Pension Continuity' : Pension7
}

section_K = {
    'Waist and Hip Measure' : Physic1,
    'Waist and Hip Measure Incomplete' : Physic2,
    'Sitting Height' : Physic3,
    'Sitting Height Incomplete' : Physic4,
    'Balance Test' : Physic5,
    'Balance Test Incomplete' : Physic6,
    'Blood Pressure Measure' : Physic7,
    'Blood Pressure Measure Incomplete' : Physic8,
    'Timed Walk Measure' : Physic9,
    'Timed Walk Measure Incomplete' : Physic10,
    'Hand Grip Measure' : Physic11,
    'Hand Grip Measure Incomplete' : Physic12
}

section_L = {
    'ADL Help' : Assitan1,
    'IADL Help' : Assitan2,
    'Personal Aids' : Assitan3,
    'Future ADL Help' : Assitan4,
    'ADL Any Care' : Assitan5,
    'ADL Informal Care' : Assitan6,
    'ADL Informal Care Spouse' : Assitan7,
    'ADL Care Children or Grandchildren' : Assitan8,
    'ADL Care Relatives' : Assitan9,
    'ADL Care Other Individuals' : Assitan10,
    'ADL Formal Care' : Assitan11,
    'ADL Care Paid Professional' : Assitan12,
    'IADL Any Care' : Assitan13,
    'IADL Informal Care' : Assitan14,
    'IADL Informal Care Spouse' : Assitan15,
    'IADL Care Children or Grandchildren' : Assitan16,
    'IADL Care Relatives' : Assitan17,
    'IADL Care Other Individuals' : Assitan18,
    'IADL Formal Care' : Assitan19,
    'IADL Care Paid Professional' : Assitan20,
    'ADL & IADL Any Care' : Assitan21,
    'ADL & IADL Informal Care' : Assitan22,
    'ADL & IADL Care Spouse' : Assitan23,
    'ADL & IADL Care Children or Grandchildren' : Assitan24,
    'ADL & IADL Care Relatives' : Assitan25,
    'ADL & IADL Care Other Individuals' : Assitan26, 
    'ADL & IADL Formal Care' : Assitan27,
    'ADL & IADL Care Paid Professional' : Assitan28,
    'Help Children or Grandchildren' : Assitan29,
    'Provides Care to Children or Grandchildren' : Assitan30,
    'Provides Care to Parents' : Assitan31,
    'Provides Care for Sick or Disabled Adults' : Assitan32
}

section_M = {
    'Support Spouse' : Stress1,
    'Support Children' : Stress2,
    'Support: Friends' : Stress3,
    'Experienced Death of a Child' : Stress4
}

section_O = {
    'Has a Will' : Plannin1,
    'Beneficiaries Will' : Plannin2,
    'Covered Life Insurance' : Plannin3
}

section_Q = {
    'Depressive Symptoms' : Phychos1,
    'Satisfaction Life' : Phychos2,
    'Single Life Satisfaction' : Phychos3,
    'Cantril Ladder' : Phychos4
}