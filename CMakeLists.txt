
cmake_minimum_required(VERSION 2.6 FATAL_ERROR)
project(bina)

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


add_executable(bina_run  Bina.cc ${sources} ${headers})
target_link_libraries(bina_run ${Geant4_LIBRARIES})


set(BINA_SCRIPTS
  run.mac
  geo.mac
  test.mac
  recompile
  )

foreach(_script ${BINA_SCRIPTS})
  configure_file(
    ${PROJECT_SOURCE_DIR}/${_script}
    ${PROJECT_BINARY_DIR}/${_script}
    COPYONLY
    )
endforeach()

file(COPY ${PROJECT_SOURCE_DIR}/data DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/ )

add_custom_target(BINA DEPENDS bina_run)
#find_package(OpenMP)
#if (OPENMP_FOUND)
 #   set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
 #   set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
 #   set (CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
#endif()


install(TARGETS bina_run DESTINATION bin)
