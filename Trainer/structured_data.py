import pandas
import numpy
import json

class ComandConfigData:
    """
    Container für das Laden und Bereitstellen von Comand-Konfigdaten aus verschiedenen Quellen
    """
    def __init__(self, fname):
        self.fname = fname
        self.config = pandas.DataFrame()
        self._load_config()

    def __str__(self):
        return self.config.to_string()

    def _load_config(self):
        if self.fname.lower().endswith(".xls") or self.fname.lower().endswith(".xslx"):
            self.type = "EXCEL"
            self.config = pandas.read_excel(self.fname)
        elif self.fname.lower().endswith(".json"):
            self.type = "JSON"
            with open(self.fname) as fd:
                self.config = pandas.DataFrame(json.load(fd)["data"]) # Besonderheit der URdaten-Version
        else:
            raise RuntimeError(f"ComandConfigData: Dateityp von {self.fname} nicht unterstützt")
        # Aufbereitung
        self.config = self.config.replace(numpy.nan, None)

    def to_dataframe(self, columns=None):
        """
        Dient nur der Entkoppelung, ist ein Getter!
        returns DataFrame
        """
        return self.config[columns] if columns else self.config

    def to_dict(self, columns=None):
        """
        returns: dict
        """
        return self.config.to_dataframe(columns).to_dict('records')

    def to_json(self, columns=None):
        """
        returns: json/dict
        Achtung: ohne data = []
        """
        return self.to_dataframe(columns).to_json(orient='records')

    def export_to_json_file(self, fname, columns=None):
        json.dump({"data": self.to_json(columns)}, open(fname, "w"))

    def export_to_excel_file(self, fname, columns=None):
        self.config.to_excel(fname, index=False, header=True)

# Es fehen noch die Tests! :-)