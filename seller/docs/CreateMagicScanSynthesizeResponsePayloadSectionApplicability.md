# CreateMagicScanSynthesizeResponsePayloadSectionApplicability

Deterministic (NO-AI) applicability hint for the heavyweight optional  form sections (vehicle compatibility, EU EPR / energy label, hazmat).  Computed from the resolved category + seller region via  `applicableOptionalSections`; the form pre-checks each section's  \"this item needs …\" toggle from it. Additive + best-effort.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vehicle_compat** | **bool** | eBay Motors / Parts vehicle-fitment (compatibilityList). | 
**epr** | **bool** | EU/UK Extended Producer Responsibility (packaging/e-waste schemes). | 
**energy_label** | **bool** | EU energy-efficiency label (fridges, TVs, lighting, appliances). | 
**hazmat** | **bool** | Hazmat classification (battery/aerosol/flammable/liquid/chemical). | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


