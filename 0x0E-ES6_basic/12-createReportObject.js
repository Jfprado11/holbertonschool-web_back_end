export default function createReportObject(employeesList) {
  const data = {
    allEmployees: employeesList,
    getNumberOfDepartments(list) {
      return Object.keys(list).length;
    },
  };
  return data;
}
