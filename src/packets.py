from dtypes import *

Packet_ID = {
    0: "Motion",
    1: "Session",
    2: "LapData",
    3: "Event",
    4: "Participants",
    5: "CarSetups",
    6: "CarTelemetry",
    7: "CarStatus",
    8: "FinalClassification",
    9: "LobbyInfo",
    10: "CarDamage",
    11: "SessionHistory",
    12: "TyreSets",
    13: "MotionEx",
    14: "TimeTrial",
    15: "LapPositions"
}

class Packet_structs:
    PacketHeader = Struct(
        "m_packetFormat" / Int16ul,
        "m_gameYear" / Int8ul,
        "m_gameMajorVersion" / Int8ul,
        "m_gameMinorVersion" / Int8ul,
        "m_packetVersion" / Int8ul,
        "m_packetId" / Int8ul,
        "m_sessionUID" / Int64ul,
        "m_sessionTime" / Float32l,
        "m_frameIdentifier" / Int32ul,
        "m_overallFrameIdentifier" / Int32ul,
        "m_playerCarIndex" / Int8ul,
        "m_secondaryPlayerCarIndex" / Int8ul,
    )

    CarMotionData = Struct(
        "m_worldPositionX" / float32,
        "m_worldPositionY" / float32,
        "m_worldPositionZ" / float32,
        "m_worldVelocityX" / float32,
        "m_worldVelocityY" / float32,
        "m_worldVelocityZ" / float32,
        "m_worldForwardDirX" / uint16,
        "m_worldForwardDirY" / uint16,
        "m_worldForwardDirZ" / uint16,
        "m_worldRightDirX" / uint16,
        "m_worldRightDirY" / uint16,
        "m_worldRightDirZ" / uint16,
        "m_gForceLateral" / float32,
        "m_gForceLongitudinal" / float32,
        "m_gForceVertical" / float32,
        "m_yaw" / float32,
        "m_pitch" / float32,
        "m_roll" / float32,
    )

    PacketMotionData = Struct(
        "m_header" / PacketHeader,
        "m_carMotionData" / CarMotionData[22],
    )

    MarshalZone = Struct(
        "m_zoneStart" / float32,
        "m_zoneFlag" / int8,
    )

    WeatherForecastSample = Struct(
        "m_sessionType" / uint8,
        "m_timeOffset" / uint8,
        "m_weather" / uint8,
        "m_trackTemperature" / int8,
        "m_trackTemperatureChange" / int8,
        "m_airTemperature" / int8,
        "m_airTemperatureChange" / int8,
        "m_rainPercentage" / uint8,
    )

    PacketSessionData = Struct(
        "m_header" / PacketHeader,
        "m_weather" / uint8,
        "m_trackTemperature" / int8,
        "m_airTemperature" / int8,
        "m_totalLaps" / uint8,
        "m_trackLength" / uint16,
        "m_sessionType" / uint8,
        "m_trackId" / int8,
        "m_formula" / uint8,
        "m_sessionTimeLeft" / uint16,
        "m_sessionDuration" / uint16,
        "m_pitSpeedLimit" / uint8,
        "m_gamePaused" / uint8,
        "m_isSpectating" / uint8,
        "m_spectatorCarIndex" / uint8,
        "m_sliProNativeSupport" / uint8,
        "m_numMarshalZones" / uint8,
        "m_marshalZones" / MarshalZone[21],
        "m_safetyCarStatus" / uint8,
        "m_networkGame" / uint8,
        "m_numWeatherForecastSamples" / uint8,
        "m_weatherForecastSamples" / WeatherForecastSample[64],
        "m_forecastAccuracy" / uint8,
        "m_aiDifficulty" / uint8,
        "m_seasonLinkIdentifier" / uint32,
        "m_weekendLinkIdentifier" / uint32,
        "m_sessionLinkIdentifier" / uint32,
        "m_pitStopWindowIdealLap" / uint8,
        "m_pitStopWindowLatestLap" / uint8,
        "m_pitStopRejoinPosition" / uint8,
        "m_steeringAssist" / uint8,
        "m_brakingAssist" / uint8,
        "m_gearboxAssist" / uint8,
        "m_pitAssist" / uint8,
        "m_pitReleaseAssist" / uint8,
        "m_ERSAssist" / uint8,
        "m_DRSAssist" / uint8,
        "m_dynamicRacingLine" / uint8,
        "m_dynamicRacingLineType" / uint8,
        "m_gameMode" / uint8,
        "m_ruleSet" / uint8,
        "m_timeOfDay" / uint32,
        "m_sessionLength" / uint8,
        "m_speedUnitsLeadPlayer" / uint8,
        "m_temperatureUnitsLeadPlayer" / uint8,
        "m_speedUnitsSecondaryPlayer" / uint8,
        "m_temperatureUnitsSecondaryPlayer" / uint8,
        "m_numSafetyCarPeriods" / uint8,
        "m_numVirtualSafetyCarPeriods" / uint8,
        "m_numRedFlagPeriods" / uint8,
        "m_equalCarPerformance" / uint8,
        "m_recoveryMode" / uint8,
        "m_flashbackLimit" / uint8,
        "m_surfaceType" / uint8,
        "m_lowFuelMode" / uint8,
        "m_raceStarts" / uint8,
        "m_tyreTemperature" / uint8,
        "m_pitLaneTyreSim" / uint8,
        "m_carDamage" / uint8,
        "m_carDamageRate" / uint8,
        "m_collisions" / uint8,
        "m_collisionsOffForFirstLapOnly" / uint8,
        "m_mpUnsafePitRelease" / uint8,
        "m_mpOffForGriefing" / uint8,
        "m_cornerCuttingStringency" / uint8,
        "m_parcFermeRules" / uint8,
        "m_pitStopExperience" / uint8,
        "m_safetyCar" / uint8,
        "m_safetyCarExperience" / uint8,
        "m_formationLap" / uint8,
        "m_formationLapExperience" / uint8,
        "m_redFlags" / uint8,
        "m_affectsLicenceLevelSolo" / uint8,
        "m_affectsLicenceLevelMP" / uint8,
        "m_numSessionsInWeekend" / uint8,
        "m_weekendStructure" / uint8[12],
        "m_sector2LapDistanceStart" / float32,
        "m_sector3LapDistanceStart" / float32,
    )

    LapData = Struct(
        "m_lastLapTimeInMS" / uint32,
        "m_currentLapTimeInMS" / uint32,
        "m_sector1TimeMSPart" / uint16,
        "m_sector1TimeMinutesPart" / uint8,
        "m_sector2TimeMSPart" / uint16,
        "m_sector2TimeMinutesPart" / uint8,
        "m_deltaToCarInFrontMSPart" / uint16,
        "m_deltaToCarInFrontMinutesPart // Time delta to car in front whole minute part" / uint8,
        "m_deltaToRaceLeaderMSPart" / uint16,
        "m_deltaToRaceLeaderMinutesPart // Time delta to race leader whole minute part" / uint8,
        "m_lapDistance" / float32,
        "m_totalDistance" / float32,
        "m_safetyCarDelta" / float32,
        "m_carPosition" / uint8,
        "m_currentLapNum" / uint8,
        "m_pitStatus" / uint8,
        "m_numPitStops" / uint8,
        "m_sector" / uint8,
        "m_currentLapInvalid" / uint8,
        "m_penalties" / uint8,
        "m_totalWarnings" / uint8,
        "m_cornerCuttingWarnings" / uint8,
        "m_numUnservedDriveThroughPens" / uint8,
        "m_numUnservedStopGoPens" / uint8,
        "m_gridPosition" / uint8,
        "m_driverStatus" / uint8,
        "m_resultStatus" / uint8,
        "m_pitLaneTimerActive" / uint8,
        "m_pitLaneTimeInLaneInMS" / uint16,
        "m_pitStopTimerInMS" / uint16,
        "m_pitStopShouldServePen" / uint8,
        "m_speedTrapFastestSpeed" / float32,
        "m_speedTrapFastestLap" / uint8,
    )

    PacketLapData = Struct(
        "m_header" / PacketHeader,
        "m_lapData" / LapData[22],
        "m_timeTrialPBCarIdx" / uint8,
        "m_timeTrialRivalCarIdx" / uint8,
    )

    EventDataDetails = Struct(
        "FastestLap" / Struct(
            "vehicleIdx" / uint8,
            "lapTime"/ float32,
        ),

        "Retirement" / Struct(
            "vehicleIdx" / uint8,
            "reason" / uint8,
        ),

        "DRSDisabled" / Struct(
            "reason" / uint8,
        ),

        "TeamMateInPits" / Struct(
            "vehicleIdx" / uint8,
        ),

        "RaceWinner" / Struct(
            "vehicleIdx" / uint8,
        ),

        "Penalty" / Struct(
            "penaltyType" / uint8,
            "infringementType" / uint8,
            "vehicleIdx" / uint8,
            "otherVehicleIdx" / uint8,
            "time" / uint8,
            "lapNum" / uint8,
            "placesGained" / uint8,
        ),

        "SpeedTrap" / Struct(
            "vehicleIdx" / uint8,
            "speed" / float32,
            "isOverallFastestInSession" / uint8,
            "isDriverFastestInSession" / uint8,
            "fastestVehicleIdxInSession" / uint8,
            "fastestSpeedInSession" / float32,
        ),

        "StartLights" / Struct(
            "numLights" / uint8,
        ),

        "DriveThroughPenaltyServed" / Struct(
            "vehicleIdx" / uint8,
        ),

        "StopGoPenaltyServed" / Struct(
            "vehicleIdx" / uint8,
            "stopTime" / float32,
        ),

        "Flashback" / Struct(
            "flashbackFrameIdentifier" / uint32,
            "flashbackSessionTime" / float32,
        ),

        "Buttons" / Struct(
            "buttonStatus" / uint32,
        ),

        "Overtake" / Struct(
            "overtakingVehicleIdx" / uint8,
            "beingOvertakenVehicleIdx" / uint8,
        ),

        "SafetyCar" / Struct(
            "safetyCarType" / uint8,
            "eventType" / uint8,
        ),

        "Collision" / Struct(
            "vehicle1Idx" / uint8,
            "vehicle2Idx" / uint8,
        )
    )

    PacketEventData = Struct(
        "m_header" / PacketHeader,
        "m_eventStringCode" / uint8[4],
        "m_eventDetails" / EventDataDetails,
    )

    LiveryColour = Struct(
        "red" / uint8,
        "green" / uint8,
        "blue" / uint8,
    )

    ParticipantData = Struct(
        "m_aiControlled" / uint8,
        "m_driverId" / uint8,
        "m_networkId" / uint8,
        "m_teamId" / uint8,
        "m_myTeam" / uint8,
        "m_raceNumber" / uint8,
        "m_nationality" / uint8,
        "m_name" / int8[32], # Null-terminated UTF-8 string
        "m_yourTelemetry" / uint8,
        "m_showOnlineNames" / uint8,
        "m_techLevel" / uint16,
        "m_platform" / uint8,
        "m_numColours" / uint8,
        "m_liveryColours" / LiveryColour[4],
    )

    PacketParticipantsData = Struct(
        "m_header" / PacketHeader,
        "m_numActiveCars" / uint8,
        "m_participants" / ParticipantData[22],
    )

    CarSetupData = Struct(
        "m_frontWing" / uint8,
        "m_rearWing" / uint8,
        "m_onThrottle" / uint8,
        "m_offThrottle" / uint8,
        "m_frontCamber" / float32,
        "m_rearCamber" / float32,
        "m_frontToe" / float32,
        "m_rearToe" / float32,
        "m_frontSuspension" / uint8,
        "m_rearSuspension" / uint8,
        "m_frontAntiRollBar" / uint8,
        "m_rearAntiRollBar" / uint8,
        "m_frontSuspensionHeight" / uint8,
        "m_rearSuspensionHeight" / uint8,
        "m_brakePressure" / uint8,
        "m_brakeBias" / uint8,
        "m_engineBraking" / uint8,
        "m_rearLeftTyrePressure" / float32,
        "m_rearRightTyrePressure" / float32,
        "m_frontLeftTyrePressure" / float32,
        "m_frontRightTyrePressure" / float32,
        "m_ballast" / uint8,
        "m_fuelLoad" / float32,
    )

    PacketCarSetupData = Struct(
        "m_header" / PacketHeader,
        "m_carSetups" / CarSetupData[22],
        "m_nextFrontWingValue" / float32,
    )

    CarTelemetryData = Struct(
        "m_speed" / uint16,
        "m_throttle" / float32,
        "m_steer" / float32,
        "m_brake" / float32,
        "m_clutch" / uint8,
        "m_gear" / int8,
        "m_engineRPM" / uint16,
        "m_drs" / uint8,
        "m_revLightsPercent" / uint8,
        "m_revLightsBitValue" / uint16,
        "m_brakesTemperature" / uint16[4],
        "m_tyresSurfaceTemperature" / uint8[4],
        "m_tyresInnerTemperature" / uint8[4],
        "m_engineTemperature" / uint16,
        "m_tyresPressure" / float32[4],
        "m_surfaceType" / uint8[4],
    )

    PacketCarTelemetryData = Struct(
        "m_header" / PacketHeader,
        "m_carTelemetryData" / CarTelemetryData[22],
        "m_mfdPanelIndex" / uint8,
        "m_mfdPanelIndexSecondaryPlayer" / uint8,
        "m_suggestedGear" / int8,
    )

    CarStatusData = Struct(
        "m_tractionControl" / uint8,
        "m_antiLockBrakes" / uint8,
        "m_fuelMix" / uint8,
        "m_frontBrakeBias" / uint8,
        "m_pitLimiterStatus" / uint8,
        "m_fuelInTank" / float32,
        "m_fuelCapacity" / float32,
        "m_fuelRemainingLaps" / float32,
        "m_maxRPM" / uint16,
        "m_idleRPM" / uint16,
        "m_maxGears" / uint8,
        "m_drsAllowed" / uint8,
        "m_drsActivationDistance" / uint16,
        "m_actualTyreCompound" / uint8,
        "m_visualTyreCompound" / uint8,
        "m_tyresAgeLaps" / uint8,
        "m_vehicleFiaFlags" / int8,
        "m_enginePowerICE" / float32,
        "m_enginePowerMGUK" / float32,
        "m_ersStoreEnergy" / float32,
        "m_ersDeployMode" / uint8,
        "m_ersHarvestedThisLapMGUK" / float32,
        "m_ersHarvestedThisLapMGUH" / float32,
        "m_ersDeployedThisLap" / float32,
        "m_networkPaused" / uint8,
    )

    PacketCarStatusData = Struct(
        "m_header" / PacketHeader,
        "m_carStatusData" / CarStatusData[22],
    )

    FinalClassificationData = Struct(
        "m_position" / uint8,
        "m_numLaps" / uint8,
        "m_gridPosition" / uint8,
        "m_points" / uint8,
        "m_numPitStops" / uint8,
        "m_resultStatus" / uint8,
        "m_resultReason" / uint8,
        "m_bestLapTimeInMS" / uint32,
        "m_totalRaceTime" / double,
        "m_penaltiesTime" / uint8,
        "m_numPenalties" / uint8,
        "m_numTyreStints" / uint8,
        "m_tyreStintsActual" / uint8[8],
        "m_tyreStintsVisual" / uint8[8],
        "m_tyreStintsEndLaps" / uint8[8],
    )

    PacketFinalClassificationData = Struct(
        "m_header" / PacketHeader,
        "m_numCars" / uint8,
        "m_classificationData" / FinalClassificationData[22],
    )

    LobbyInfoData = Struct(
        "m_aiControlled" / uint8,
        "m_teamId" / uint8,
        "m_nationality" / uint8,
        "m_platform" / uint8,
        "m_name" / int8[32],
        "m_carNumber" / uint8,
        "m_yourTelemetry" / uint8,
        "m_showOnlineNames" / uint8,
        "m_techLevel" / uint16,
        "m_readyStatus" / uint8,
    )

    PacketLobbyInfoData = Struct(
        "m_header" / PacketHeader,
        "m_numPlayers" / uint8,
        "m_lobbyPlayers" / LobbyInfoData[22],
    )

    CarDamageData = Struct(
        "m_tyresWear" / float32[4],
        "m_tyresDamage" / uint8[4],
        "m_brakesDamage" / uint8[4],
        "m_tyreBlisters" / uint8[4],
        "m_frontLeftWingDamage" / uint8,
        "m_frontRightWingDamage" / uint8,
        "m_rearWingDamage" / uint8,
        "m_floorDamage" / uint8,
        "m_diffuserDamage" / uint8,
        "m_sidepodDamage" / uint8,
        "m_drsFault" / uint8,
        "m_ersFault" / uint8,
        "m_gearBoxDamage" / uint8,
        "m_engineDamage" / uint8,
        "m_engineMGUHWear" / uint8,
        "m_engineESWear" / uint8,
        "m_engineCEWear" / uint8,
        "m_engineICEWear" / uint8,
        "m_engineMGUKWear" / uint8,
        "m_engineTCWear" / uint8,
        "m_engineBlown" / uint8,
        "m_engineSeized" / uint8,
    )

    PacketCarDamageData = Struct(
        "m_header" / PacketHeader,
        "m_carDamageData" / CarDamageData[22],
    )

    LapHistoryData = Struct(
        "m_lapTimeInMS" / uint32,
        "m_sector1TimeMSPart" / uint16,
        "m_sector1TimeMinutesPart" / uint8,
        "m_sector2TimeMSPart" / uint16,
        "m_sector2TimeMinutesPart" / uint8,
        "m_sector3TimeMSPart" / uint16,
        "m_sector3TimeMinutesPart" / uint8,
        "m_lapValidBitFlags" / uint8,
    )

    TyreStintHistoryData = Struct(
        "m_endLap" / uint8,
        "m_tyreActualCompound" / uint8,
        "m_tyreVisualCompound" / uint8,
    )

    PacketSessionHistoryData = Struct(
        "m_header" / PacketHeader,
        "m_carIdx" / uint8,
        "m_numLaps" / uint8,
        "m_numTyreStints" / uint8,
        "m_bestLapTimeLapNum" / uint8,
        "m_bestSector1LapNum" / uint8,
        "m_bestSector2LapNum" / uint8,
        "m_bestSector3LapNum" / uint8,
        "m_lapHistoryData" / LapHistoryData[100],
        "m_tyreStintsHistoryData" / TyreStintHistoryData[8],
    )

    TyreSetData = Struct(
        "m_actualTyreCompound" / uint8,
        "m_visualTyreCompound" / uint8,
        "m_wear" / uint8,
        "m_available" / uint8,
        "m_recommendedSession" / uint8,
        "m_lifeSpan" / uint8,
        "m_usableLife" / uint8,
        "m_lapDeltaTime" / int16,
        "m_fitted" / uint8,
    )

    PacketTyreSetsData = Struct(
        "m_header" / PacketHeader,
        "m_carIdx" / uint8,
        "m_tyreSetData" / TyreSetData[20],
        "m_fittedIdx" / uint8,
    )

    PacketMotionExData = Struct(
        "m_header" / PacketHeader,
        "m_suspensionPosition" / float32[4],
        "m_suspensionVelocity" / float32[4],
        "m_suspensionAcceleration" / float32[4],
        "m_wheelSpeed" / float32[4],
        "m_wheelSlipRatio" / float32[4],
        "m_wheelSlipAngle" / float32[4],
        "m_wheelLatForce" / float32[4],
        "m_wheelLongForce" / float32[4],
        "m_heightOfCOGAboveGround" / float32,
        "m_localVelocityX" / float32,
        "m_localVelocityY" / float32,
        "m_localVelocityZ" / float32,
        "m_angularVelocityX" / float32,
        "m_angularVelocityY" / float32,
        "m_angularVelocityZ" / float32,
        "m_angularAccelerationX" / float32,
        "m_angularAccelerationY" / float32,
        "m_angularAccelerationZ" / float32,
        "m_frontWheelsAngle" / float32,
        "m_wheelVertForce" / float32[4],
        "m_frontAeroHeight" / float32,
        "m_rearAeroHeight" / float32,
        "m_frontRollAngle" / float32,
        "m_rearRollAngle" / float32,
        "m_chassisYaw" / float32,
        "m_chassisPitch" / float32,
        "m_wheelCamber" / float32[4],
        "m_wheelCamberGain" / float32[4],
    )

    TimeTrialDataSet = Struct(
        "m_carIdx" / uint8,
        "m_teamId" / uint8,
        "m_lapTimeInMS" / uint32,
        "m_sector1TimeInMS" / uint32,
        "m_sector2TimeInMS" / uint32,
        "m_sector3TimeInMS" / uint32,
        "m_tractionControl" / uint8,
        "m_gearboxAssist" / uint8,
        "m_antiLockBrakes" / uint8,
        "m_equalCarPerformance" / uint8,
        "m_customSetup" / uint8,
        "m_valid" / uint8,
    )

    PacketTimeTrialData = Struct(
        "m_header" / PacketHeader,
        "m_playerSessionBestDataset" / TimeTrialDataSet,
        "m_personalBestDataSet" / TimeTrialDataSet,
        "m_rivalDataSet" / TimeTrialDataSet,
    )

    PacketLapPositionsData = Struct(
        "m_header" / PacketHeader,
        "m_numLaps" / uint8,
        "m_lapStart" / uint8,
        "m_positionForVehicleIdx" / uint8[50][22],
    )
