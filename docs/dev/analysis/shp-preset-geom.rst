
``CT_PresetGeometry2D``
=======================

.. highlight:: xml

.. csv-table::
   :header-rows: 0
   :stub-columns: 1
   :widths: 15, 50

   Spec Name    , Preset Geometry
   Tag(s)       , a:prstGeom
   Namespace    , drawingml (dml-main.xsd)
   Spec Section , 20.1.9.18


Spec text
---------

   This element specifies when a preset geometric shape should be used instead
   of a custom geometric shape. The generating application should be able to
   render all preset geometries enumerated in the ST_ShapeType list.


Schema excerpt
--------------

::

  <xsd:complexType name="CT_PresetGeometry2D">
    <xsd:sequence>
      <xsd:element name="avLst" type="CT_GeomGuideList" minOccurs="0"/>
    </xsd:sequence>
    <xsd:attribute name="prst" type="ST_ShapeType" use="required"/>
  </xsd:complexType>

  <xsd:complexType name="CT_GeomGuideList">
    <xsd:sequence>
      <xsd:element name="gd" type="CT_GeomGuide" minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="CT_GeomGuide">
    <xsd:attribute name="name" type="ST_GeomGuideName"    use="required"/>
    <xsd:attribute name="fmla" type="ST_GeomGuideFormula" use="required"/>
  </xsd:complexType>

  <xsd:simpleType name="ST_GeomGuideName">
    <xsd:restriction base="xsd:token"/>
  </xsd:simpleType>

  <xsd:simpleType name="ST_GeomGuideFormula">
    <xsd:restriction base="xsd:string"/>
  </xsd:simpleType>

  <xsd:simpleType name="ST_ShapeType">
    <xsd:restriction base="xsd:token">
      <xsd:enumeration value="line"/>
      <xsd:enumeration value="lineInv"/>
      <xsd:enumeration value="triangle"/>
      <xsd:enumeration value="rtTriangle"/>
      <xsd:enumeration value="rect"/>
      <xsd:enumeration value="diamond"/>
      <xsd:enumeration value="parallelogram"/>
      <xsd:enumeration value="trapezoid"/>
      <xsd:enumeration value="nonIsoscelesTrapezoid"/>
      <xsd:enumeration value="pentagon"/>
      <xsd:enumeration value="hexagon"/>
      <xsd:enumeration value="heptagon"/>
      <xsd:enumeration value="octagon"/>
      <xsd:enumeration value="decagon"/>
      <xsd:enumeration value="dodecagon"/>
      <xsd:enumeration value="star4"/>
      <xsd:enumeration value="star5"/>
      <xsd:enumeration value="star6"/>
      <xsd:enumeration value="star7"/>
      <xsd:enumeration value="star8"/>
      <xsd:enumeration value="star10"/>
      <xsd:enumeration value="star12"/>
      <xsd:enumeration value="star16"/>
      <xsd:enumeration value="star24"/>
      <xsd:enumeration value="star32"/>
      <xsd:enumeration value="roundRect"/>
      <xsd:enumeration value="round1Rect"/>
      <xsd:enumeration value="round2SameRect"/>
      <xsd:enumeration value="round2DiagRect"/>
      <xsd:enumeration value="snipRoundRect"/>
      <xsd:enumeration value="snip1Rect"/>
      <xsd:enumeration value="snip2SameRect"/>
      <xsd:enumeration value="snip2DiagRect"/>
      <xsd:enumeration value="plaque"/>
      <xsd:enumeration value="ellipse"/>
      <xsd:enumeration value="teardrop"/>
      <xsd:enumeration value="homePlate"/>
      <xsd:enumeration value="chevron"/>
      <xsd:enumeration value="pieWedge"/>
      <xsd:enumeration value="pie"/>
      <xsd:enumeration value="blockArc"/>
      <xsd:enumeration value="donut"/>
      <xsd:enumeration value="noSmoking"/>
      <xsd:enumeration value="rightArrow"/>
      <xsd:enumeration value="leftArrow"/>
      <xsd:enumeration value="upArrow"/>
      <xsd:enumeration value="downArrow"/>
      <xsd:enumeration value="stripedRightArrow"/>
      <xsd:enumeration value="notchedRightArrow"/>
      <xsd:enumeration value="bentUpArrow"/>
      <xsd:enumeration value="leftRightArrow"/>
      <xsd:enumeration value="upDownArrow"/>
      <xsd:enumeration value="leftUpArrow"/>
      <xsd:enumeration value="leftRightUpArrow"/>
      <xsd:enumeration value="quadArrow"/>
      <xsd:enumeration value="leftArrowCallout"/>
      <xsd:enumeration value="rightArrowCallout"/>
      <xsd:enumeration value="upArrowCallout"/>
      <xsd:enumeration value="downArrowCallout"/>
      <xsd:enumeration value="leftRightArrowCallout"/>
      <xsd:enumeration value="upDownArrowCallout"/>
      <xsd:enumeration value="quadArrowCallout"/>
      <xsd:enumeration value="bentArrow"/>
      <xsd:enumeration value="uturnArrow"/>
      <xsd:enumeration value="circularArrow"/>
      <xsd:enumeration value="leftCircularArrow"/>
      <xsd:enumeration value="leftRightCircularArrow"/>
      <xsd:enumeration value="curvedRightArrow"/>
      <xsd:enumeration value="curvedLeftArrow"/>
      <xsd:enumeration value="curvedUpArrow"/>
      <xsd:enumeration value="curvedDownArrow"/>
      <xsd:enumeration value="swooshArrow"/>
      <xsd:enumeration value="cube"/>
      <xsd:enumeration value="can"/>
      <xsd:enumeration value="lightningBolt"/>
      <xsd:enumeration value="heart"/>
      <xsd:enumeration value="sun"/>
      <xsd:enumeration value="moon"/>
      <xsd:enumeration value="smileyFace"/>
      <xsd:enumeration value="irregularSeal1"/>
      <xsd:enumeration value="irregularSeal2"/>
      <xsd:enumeration value="foldedCorner"/>
      <xsd:enumeration value="bevel"/>
      <xsd:enumeration value="frame"/>
      <xsd:enumeration value="halfFrame"/>
      <xsd:enumeration value="corner"/>
      <xsd:enumeration value="diagStripe"/>
      <xsd:enumeration value="chord"/>
      <xsd:enumeration value="arc"/>
      <xsd:enumeration value="leftBracket"/>
      <xsd:enumeration value="rightBracket"/>
      <xsd:enumeration value="leftBrace"/>
      <xsd:enumeration value="rightBrace"/>
      <xsd:enumeration value="bracketPair"/>
      <xsd:enumeration value="bracePair"/>
      <xsd:enumeration value="straightConnector1"/>
      <xsd:enumeration value="bentConnector2"/>
      <xsd:enumeration value="bentConnector3"/>
      <xsd:enumeration value="bentConnector4"/>
      <xsd:enumeration value="bentConnector5"/>
      <xsd:enumeration value="curvedConnector2"/>
      <xsd:enumeration value="curvedConnector3"/>
      <xsd:enumeration value="curvedConnector4"/>
      <xsd:enumeration value="curvedConnector5"/>
      <xsd:enumeration value="callout1"/>
      <xsd:enumeration value="callout2"/>
      <xsd:enumeration value="callout3"/>
      <xsd:enumeration value="accentCallout1"/>
      <xsd:enumeration value="accentCallout2"/>
      <xsd:enumeration value="accentCallout3"/>
      <xsd:enumeration value="borderCallout1"/>
      <xsd:enumeration value="borderCallout2"/>
      <xsd:enumeration value="borderCallout3"/>
      <xsd:enumeration value="accentBorderCallout1"/>
      <xsd:enumeration value="accentBorderCallout2"/>
      <xsd:enumeration value="accentBorderCallout3"/>
      <xsd:enumeration value="wedgeRectCallout"/>
      <xsd:enumeration value="wedgeRoundRectCallout"/>
      <xsd:enumeration value="wedgeEllipseCallout"/>
      <xsd:enumeration value="cloudCallout"/>
      <xsd:enumeration value="cloud"/>
      <xsd:enumeration value="ribbon"/>
      <xsd:enumeration value="ribbon2"/>
      <xsd:enumeration value="ellipseRibbon"/>
      <xsd:enumeration value="ellipseRibbon2"/>
      <xsd:enumeration value="leftRightRibbon"/>
      <xsd:enumeration value="verticalScroll"/>
      <xsd:enumeration value="horizontalScroll"/>
      <xsd:enumeration value="wave"/>
      <xsd:enumeration value="doubleWave"/>
      <xsd:enumeration value="plus"/>
      <xsd:enumeration value="flowChartProcess"/>
      <xsd:enumeration value="flowChartDecision"/>
      <xsd:enumeration value="flowChartInputOutput"/>
      <xsd:enumeration value="flowChartPredefinedProcess"/>
      <xsd:enumeration value="flowChartInternalStorage"/>
      <xsd:enumeration value="flowChartDocument"/>
      <xsd:enumeration value="flowChartMultidocument"/>
      <xsd:enumeration value="flowChartTerminator"/>
      <xsd:enumeration value="flowChartPreparation"/>
      <xsd:enumeration value="flowChartManualInput"/>
      <xsd:enumeration value="flowChartManualOperation"/>
      <xsd:enumeration value="flowChartConnector"/>
      <xsd:enumeration value="flowChartPunchedCard"/>
      <xsd:enumeration value="flowChartPunchedTape"/>
      <xsd:enumeration value="flowChartSummingJunction"/>
      <xsd:enumeration value="flowChartOr"/>
      <xsd:enumeration value="flowChartCollate"/>
      <xsd:enumeration value="flowChartSort"/>
      <xsd:enumeration value="flowChartExtract"/>
      <xsd:enumeration value="flowChartMerge"/>
      <xsd:enumeration value="flowChartOfflineStorage"/>
      <xsd:enumeration value="flowChartOnlineStorage"/>
      <xsd:enumeration value="flowChartMagneticTape"/>
      <xsd:enumeration value="flowChartMagneticDisk"/>
      <xsd:enumeration value="flowChartMagneticDrum"/>
      <xsd:enumeration value="flowChartDisplay"/>
      <xsd:enumeration value="flowChartDelay"/>
      <xsd:enumeration value="flowChartAlternateProcess"/>
      <xsd:enumeration value="flowChartOffpageConnector"/>
      <xsd:enumeration value="actionButtonBlank"/>
      <xsd:enumeration value="actionButtonHome"/>
      <xsd:enumeration value="actionButtonHelp"/>
      <xsd:enumeration value="actionButtonInformation"/>
      <xsd:enumeration value="actionButtonForwardNext"/>
      <xsd:enumeration value="actionButtonBackPrevious"/>
      <xsd:enumeration value="actionButtonEnd"/>
      <xsd:enumeration value="actionButtonBeginning"/>
      <xsd:enumeration value="actionButtonReturn"/>
      <xsd:enumeration value="actionButtonDocument"/>
      <xsd:enumeration value="actionButtonSound"/>
      <xsd:enumeration value="actionButtonMovie"/>
      <xsd:enumeration value="gear6"/>
      <xsd:enumeration value="gear9"/>
      <xsd:enumeration value="funnel"/>
      <xsd:enumeration value="mathPlus"/>
      <xsd:enumeration value="mathMinus"/>
      <xsd:enumeration value="mathMultiply"/>
      <xsd:enumeration value="mathDivide"/>
      <xsd:enumeration value="mathEqual"/>
      <xsd:enumeration value="mathNotEqual"/>
      <xsd:enumeration value="cornerTabs"/>
      <xsd:enumeration value="squareTabs"/>
      <xsd:enumeration value="plaqueTabs"/>
      <xsd:enumeration value="chartX"/>
      <xsd:enumeration value="chartStar"/>
      <xsd:enumeration value="chartPlus"/>
    </xsd:restriction>
