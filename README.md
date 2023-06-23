# zoho-connector
Connector to the Zoho CRM

## Developer notes
The `.authconfig` file needs `client_id` and `client_secret` properties.

## Fields

Extracted from the fields metadata api

```
Leads : Annual_Revenue,City,Company,Converted_Account,Converted_Contact,Converted_Deal,Country,Created_By,Created_Time,Description,Designation,Email,Email_Opt_Out,Enrich_Status__s,Fax,First_Name,Full_Name,Industry,Last_Activity_Time,Last_Enriched_Time__s,Last_Name,Lead_Conversion_Time,Lead_Source,Lead_Status,Mobile,Modified_By,Modified_Time,No_of_Employees,Owner,Phone,Rating,Record_Image,Salutation,Secondary_Email,Skype_ID,State,Street,Twitter,Unsubscribed_Mode,Unsubscribed_Time,Website,Zip_Code
Accounts : Account_Name,Account_Number,Account_Site,Account_Type,Annual_Revenue,Billing_City,Billing_Code,Billing_Country,Billing_State,Billing_Street,Created_By,Created_Time,Description,Employees,Enrich_Status__s,Fax,Industry,Last_Activity_Time,Last_Enriched_Time__s,Modified_By,Modified_Time,Owner,Ownership,Parent_Account,Phone,Rating,Record_Image,SIC_Code,Shipping_City,Shipping_Code,Shipping_Country,Shipping_State,Shipping_Street,Ticker_Symbol,Website
Contacts : Account_Name,Assistant,Asst_Phone,Created_By,Created_Time,Date_of_Birth,Department,Description,Email,Email_Opt_Out,Enrich_Status__s,Fax,First_Name,Full_Name,Home_Phone,Last_Activity_Time,Last_Enriched_Time__s,Last_Name,Lead_Source,Mailing_City,Mailing_Country,Mailing_State,Mailing_Street,Mailing_Zip,Mobile,Modified_By,Modified_Time,Other_City,Other_Country,Other_Phone,Other_State,Other_Street,Other_Zip,Owner,Phone,Record_Image,Reporting_To,Salutation,Secondary_Email,Skype_ID,Title,Twitter,Unsubscribed_Mode,Unsubscribed_Time
Deals : Account_Name,Amount,Campaign_Source,Closing_Date,Contact_Name,Created_By,Created_Time,Deal_Name,Description,Expected_Revenue,Last_Activity_Time,Lead_Conversion_Time,Lead_Source,Modified_By,Modified_Time,Next_Step,Overall_Sales_Duration,Owner,Probability,Sales_Cycle_Duration,Stage,Type
Campaigns : Actual_Cost,Budgeted_Cost,Campaign_Name,Created_By,Created_Time,Description,End_Date,Expected_Response,Expected_Revenue,Modified_By,Modified_Time,Num_sent,Owner,Parent_Campaign,Start_Date,Status,Type
Tasks : Closed_Time,Created_By,Created_Time,Description,Due_Date,Modified_By,Modified_Time,Owner,Priority,Recurring_Activity,Remind_At,Send_Notification_Email,Status,Subject,What_Id,Who_Id
Events : All_day,Check_In_Address,Check_In_By,Check_In_City,Check_In_Comment,Check_In_Country,Check_In_State,Check_In_Status,Check_In_Sub_Locality,Check_In_Time,Created_By,Created_Time,Description,End_DateTime,Event_Title,Latitude,Longitude,Modified_By,Modified_Time,Owner,Participants,Recurring_Activity,Start_DateTime,Venue,What_Id,Who_Id,ZIP_Code
```

## Notes

* Only modules available in the free tier has been implemented (Contacts, Accounts and Deals)
* Webhooks, paging and continuation support has not been implemented yet