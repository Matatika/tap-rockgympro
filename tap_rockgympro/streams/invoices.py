from tap_rockgympro.utils import format_date_transaction_iso, format_transaction_date
from tap_rockgympro.mixins import FacilityStream


class Invoices(FacilityStream):
    def format_record(self, record, facility_code):
        if 'customerGuid' not in record or not record['customerGuid']:
            # We require a customer GUID for the records to work
            return

        record['invoicePostDate'] = format_date_transaction_iso(record['invoicePostDate'], self.get_timezone(facility_code))
        if record['payment']:
            record['payment']['postdate'] = format_date_transaction_iso(record['payment']['postdate'], self.get_timezone(facility_code))
        record['facilityCode'] = facility_code
        return record

    def get_updated_time(self, record, facility_code):
        return format_transaction_date(record['invoicePostDate'], self.get_timezone(facility_code))

    def get_created_time(self, record, facility_code):
        return format_transaction_date(record['invoicePostDate'], self.get_timezone(facility_code))

    def get_url(self, code, page, bookmark_time):
        url = super().get_url(code, page, bookmark_time)

        if bookmark_time:
            url += '&startDateTime=' + bookmark_time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            url +=  '&startDateTime=2025-01-01 00:00:00'

        return url
