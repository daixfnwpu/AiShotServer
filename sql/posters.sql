{
  "formatVersion": 1,
  "database": {
    "version": 1,
    "identityHash": "80d749a4d002ddbab801d2e5f0f5eedf",
    "entities": [
      {
        "tableName": "Poster",
        "createSql": "CREATE TABLE IF NOT EXISTS `${TABLE_NAME}` (`id` INTEGER NOT NULL, `name` TEXT NOT NULL, `release` TEXT NOT NULL, `playtime` TEXT NOT NULL, `description` TEXT NOT NULL, `plot` TEXT NOT NULL, `poster` TEXT NOT NULL, `gif` TEXT NOT NULL, PRIMARY KEY(`id`))",
        "fields": [
          {
            "fieldPath": "id",
            "columnName": "id",
            "affinity": "INTEGER",
            "notNull": true
          },
          {
            "fieldPath": "name",
            "columnName": "name",
            "affinity": "TEXT",
            "notNull": true
          },
          {
            "fieldPath": "release",
            "columnName": "release",
            "affinity": "TEXT",
            "notNull": true
          },
          {
            "fieldPath": "playtime",
            "columnName": "playtime",
            "affinity": "TEXT",
            "notNull": true
          },
          {
            "fieldPath": "description",
            "columnName": "description",
            "affinity": "TEXT",
            "notNull": true
          },
          {
            "fieldPath": "plot",
            "columnName": "plot",
            "affinity": "TEXT",
            "notNull": true
          },
          {
            "fieldPath": "poster",
            "columnName": "poster",
            "affinity": "TEXT",
            "notNull": true
          },
          {
            "fieldPath": "gif",
            "columnName": "gif",
            "affinity": "TEXT",
            "notNull": true
          }
        ],
        "primaryKey": {
          "columnNames": [
            "id"
          ],
          "autoGenerate": false
        },
        "indices": [],
        "foreignKeys": []
      }
    ],
    "views": [],
    "setupQueries": [
      "CREATE TABLE IF NOT EXISTS room_master_table (id INTEGER PRIMARY KEY,identity_hash TEXT)",
      "INSERT OR REPLACE INTO room_master_table (id,identity_hash) VALUES(42, '80d749a4d002ddbab801d2e5f0f5eedf')"
    ]
  }
}