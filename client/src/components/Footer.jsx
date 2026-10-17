const Footer = () => {
  return (
    <footer className="bg-primary text-white mt-auto py-3">
      <div className="container text-center">
        <small>
          &copy; {new Date().getFullYear()} CampusCare — College Complaint Management System
        </small>
      </div>
    </footer>
  );
};

export default Footer;
