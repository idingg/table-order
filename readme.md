# 서비스(음식배달, 정찰경찰 등) 로봇 및 관제 시스템 개발
서비스 로봇 및 관제 시스템은 음식배달 또는 정찰 등 다양한 서비스 업무를 자동화하는 ROS2 기반의 통합 로봇 시스템입니다. 이 프로젝트는 테이블 주문 시스템, 주방 관리, 로봇 제어, 그리고 실시간 관제 기능을 포함한 서비스 로봇 솔루션입니다.

## 주요 기능
### 1. 테이블 주문 시스템
#### 주문 인터페이스
- 테이블별 주문 관리 및 장바구니
- ROS2 서비스를 통한 주방과의 실시간 통신
- 예상 준비시간 표시

#### 주방 인터페이스
- 실시간 주문 현황 및 테이블별 주문 내역 표시
- 제조 완료 및 서빙로봇 목표 테이블 지정
- 시간대별 매출 통계 그래프 제공

### 2. 로봇 제어 시스템
- Gazebo 시뮬레이션 환경에서의 정확한 테이블 네비게이션
- 액션 기반 통신: 목적지 설정, 이동 상태 피드백, 도착 확인
- 화재 경보: 전 테이블 실시간 화재 경보 알림 시스템

### 3. 관제 및 로깅 시스템
- 다중 레벨 로깅(info, warning, error, debug, fatal)
- 목표, 위치, 작업 상태 등 로봇 상태 실시간 추적
- SQLite 기반 주문, 결제, 로봇 상태 로그 데이터 관리
- 작업별 신뢰성과 성능을 고려한 토픽/서비스/액션 QoS 최적화

## 사용 기술
- 로봇 프레임워크: <img src="https://img.shields.io/badge/ROS2-22314E?style=for-the-badge&logo=ros&logoColor=white">
- 프로그래밍 언어: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
- GUI 프레임워크: <img src="https://img.shields.io/badge/PyQt-41CD52?style=for-the-badge&logo=qt&logoColor=white">
- 데이터베이스: <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
- 시뮬레이션: <img src="https://img.shields.io/badge/Gazebo-F5820D?style=for-the-badge&logo=gazebo&logoColor=white"> <img src="https://img.shields.io/badge/RViz-22314E?style=for-the-badge&logo=ros&logoColor=white">
- 디자인 도구: <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">

## 시스템 아키텍처
### 노드
![alt text](https://github.com/idingg/table-order/blob/main/images/1.png?raw=true)

### 통신
- Topic: 화재 경보, 실시간 상태 업데이트
- Service: 주문 처리, 메뉴 관리
- Action: 로봇 네비게이션, 장거리 작업

## 활용 분야
- 서빙 로봇: 음식점에서 일반적으로 사용하는 테이블 오더 및 로봇 서빙 시스템

## 향후 개선 방향
- 실제 환경에 대한 시스템 테스트
- 로봇 배터리 상태, 주문 예상 시간 등 제공 정보 추가
- 테이블 위치 설정 기능
- 인터페이스 향상

## 담당 업무
- 진민혁: 시스템 설계, ROS2 통신, 데이터베이스 구현
- 서연우: GUI 설계, ROS2 통신 구현

## 발표 자료 주요 내용
![alt text](https://github.com/idingg/table-order/blob/main/images/dbscheme.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/1.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/2.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/3.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/4.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/5.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/6.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/7.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/8.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/9.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/10.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/11.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/12.png?raw=true)
![alt text](https://github.com/idingg/table-order/blob/main/images/13.png?raw=true)
