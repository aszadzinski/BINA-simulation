
cmake_minimum_required(VERSION 2.6 FATAL_ERROR)
project(bina_breakup2.11)

option(WITH_GEANT4_UIVIS "PACH" ON)
if(WITH_GEANT4_UIVIS)
  find_package(Geant4 REQUIRED ui_all vis_all)
else()
  find_package(Geant4 REQUIRED)
endif()

include(${Geant4_USE_FILE})
include_directories(${PROJECT_SOURCE_DIR}/include)


file(GLOB sources ${PROJECT_SOURCE_DIR}/src/*.cc)
file(GLOB headers ${PROJECT_SOURCE_DIR}/include/*.hh)


add_executable(bina_breakup2.11 bina_breakup2.11.cc ${sources} ${headers})
target_link_libraries(bina_breakup2.11 ${Geant4_LIBRARIES})


set(BINA_SCRIPTS
  run.mac
  geo.mac
  )

foreach(_script ${BINA_SCRIPTS})
  configure_file(
    ${PROJECT_SOURCE_DIR}/${_script}
    ${PROJECT_BINARY_DIR}/${_script}
    COPYONLY
    )
endforeach()


add_custom_target(BINA DEPENDS bina_breakup2.11)


install(TARGETS bina_breakup2.11 DESTINATION bin)


